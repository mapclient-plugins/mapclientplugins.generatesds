import json
import logging

import os.path
import pandas as pd

from PySide6 import QtCore, QtWidgets
from filelock import FileLock, Timeout
from mapclient.settings.general import get_data_directory
from mapclientplugins.generatesdsstep.contributorinformationwidget import ContributorInformationWidget
from mapclientplugins.generatesdsstep.definitions import GENERATE_SDS_DATABASE_FILENAME, SCAFFOLD_INFO_FILE
from mapclientplugins.generatesdsstep.otherrinformationwidget import OtherInformationWidget
from mapclientplugins.generatesdsstep.ui_generatesdswidget import Ui_GenerateSDSWidget

logger = logging.getLogger(__name__)


def _determine_location(text, index):
    parts = text.split("__")
    column = "Value" if index == 1 else f"Value {index}"
    row = " ".join(parts[2].split("_"))
    if parts[1] == "manifest":
        parts[1] = os.path.join("primary", "manifest")
        column = row
        row = SCAFFOLD_INFO_FILE
    if parts[1] == "dataset_description":
        row = f"    {row}"
    return parts[1] + ".xlsx", row, column


def _flatten(xss):
    return [x for xs in xss for x in xs]


def _populate_chip_layout(layout):
    chip_layout = []
    for row in range(layout.rowCount()):
        if layout.columnCount():
            chip_layout.append([])
        for column in range(layout.columnCount()):
            item = layout.itemAtPosition(row, column)
            if item:
                chip_layout[row].append(item.widget())

    return chip_layout


def _determine_chip_row_column(chip, widget):
    layout_column_count = []
    layout_max_width = []
    chip_layout = _populate_chip_layout(widget.layout())
    for layout_row in chip_layout:
        layout_column_count.append(len(layout_row))
        layout_max_width.append([])
        for existing_chip in layout_row:
            layout_max_width[-1].append(existing_chip.sizeHint().width())

    cur_width = chip.sizeHint().width()

    max_columns = max(layout_column_count) if len(layout_column_count) else 0
    max_entry_width = [0] * max_columns
    for i in layout_max_width:
        for index, j in enumerate(i):
            max_entry_width[index] = j if j > max_entry_width[index] else max_entry_width[index]

    row_chips = chip_layout[-1]
    if len(row_chips) < len(max_entry_width):
        max_entry_width[len(row_chips)] = cur_width
    else:
        max_entry_width.append(cur_width)

    proposed_width = sum(max_entry_width)
    spacing = 12 * len(max_entry_width) + 12

    if proposed_width + spacing > widget.size().width():
        chip_layout.append([])

    last_row = chip_layout[-1]
    last_row.append(chip)

    row = len(chip_layout) - 1
    return row, len(chip_layout[row]) - 1


def _widget_chip_texts(widget):
    layout = widget.layout()
    chip_layout = _populate_chip_layout(layout)
    chips = _flatten(chip_layout)
    return [chip.tabText(0) for chip in chips]


class GenerateSDSWidget(QtWidgets.QWidget):

    def __init__(self, dataset_loc, dataset_type, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self._ui = Ui_GenerateSDSWidget()
        self._ui.setupUi(self)
        self._ui.stackedWidgetDynamic.setCurrentIndex(1 if dataset_type == "Scaffold" else 0)
        self._ui.groupBoxDynamic.setTitle("Scaffold manifest" if dataset_type == "Scaffold" else "Subjects and Samples")
        self._ui.pushButtonAddKeyword.setEnabled(False)
        self._ui.widgetForChips__dataset_description__Keywords.setLayout(QtWidgets.QGridLayout())
        self._keyword_chips = []
        self._add_contributor_information_tab(load_database_info=False)
        self._add_other_information_tab(load_database_info=False)

        application_data_directory = get_data_directory()
        self._database = {"Contributor_information": [], "Other_information": {}}
        self._database_filename = os.path.join(application_data_directory, GENERATE_SDS_DATABASE_FILENAME)

        self._dataset_loc = dataset_loc
        self._dataset_type = dataset_type

        self._load_information()
        self._load_database()

        self._make_connections()
        self._callback = None

    def _make_connections(self):
        self._ui.pushButtonDone.clicked.connect(self._done_button_clicked)
        self._ui.pushButtonAddContributor.clicked.connect(self._add_contributor_information_tab)
        self._ui.pushButtonRemoveContributor.clicked.connect(self._remove_contributor_information_tab)
        self._ui.pushButtonAddOther.clicked.connect(self._add_other_information_tab)
        self._ui.pushButtonRemoveOther.clicked.connect(self._remove_other_information_tab)
        self._ui.databaseOnlyComboBox__dataset_description__Keywords.editTextChanged.connect(self._keywords_text_changed)
        self._ui.pushButtonAddKeyword.clicked.connect(self._add_keyword_clicked)

    def _keywords_text_changed(self, text):
        self._ui.pushButtonAddKeyword.setEnabled(text != '')

    def _remove_chip_clicked(self):
        sender = self.sender()
        widget = sender.parentWidget()
        layout = widget.layout()
        chip_layout = _populate_chip_layout(layout)
        senders = _flatten(chip_layout)
        index = senders.index(sender)
        del senders[index]

        texts = [t.tabText(0) for t in senders]

        item = layout.takeAt(0)
        while item:
            item_widget = item.widget()
            item_widget.hide()
            del item
            item = layout.takeAt(0)

        for text in texts:
            self._add_keyword(text, widget)

    def _create_chip(self, text):
        tabbar = QtWidgets.QTabBar()
        tabbar.setTabsClosable(True)
        tabbar.tabCloseRequested.connect(self._remove_chip_clicked)
        tabbar.addTab(text)
        return tabbar

    def _add_keyword_clicked(self):
        self._add_keyword(self._ui.databaseOnlyComboBox__dataset_description__Keywords.currentText(), self._ui.widgetForChips__dataset_description__Keywords)

    def _add_keyword(self, text, widget):
        chip = self._create_chip(text)
        row, column = _determine_chip_row_column(chip, widget)
        widget.layout().addWidget(chip, row, column, QtCore.Qt.AlignmentFlag.AlignHCenter)

    def _load_database(self):
        if os.path.isfile(self._database_filename):
            try:
                with FileLock(self._database_filename + ".lock", 3):
                    with open(self._database_filename) as fh:
                        self._database = json.load(fh)
            except Timeout:
                logger.info("Failed to read Generate SDS database.")

        contributor_information = self._database.get("Contributor_information", [])
        for index in range(self._ui.tabWidgetContributors.count()):
            widget = self._ui.tabWidgetContributors.widget(index)
            widget.load_database_contributor_information(contributor_information)

        other_information = self._database.get("Other_information", {})
        for index in range(self._ui.tabWidgetOthers.count()):
            widget = self._ui.tabWidgetOthers.widget(index)
            widget.load_database_other_information(other_information)

        skipped_attr = ["Contributor_information", "Other_information"]
        for attr in self._database:
            if attr not in skipped_attr:
                element = getattr(self._ui, attr, None)
                if element:
                    for item in self._database[attr]:
                        if element.findText(item) == -1:
                            element.addItem(item)

        self._ui.databaseOnlyComboBox__dataset_description__Keywords.insertItem(0, "")
        self._ui.databaseOnlyComboBox__dataset_description__Keywords.setCurrentIndex(0)

    def _save_value_to_file(self, file_destination, file_row, file_column, value):
        df = pd.read_excel(os.path.join(self._dataset_loc, file_destination), index_col=0, dtype=str).fillna("")
        df.at[file_row, file_column] = value
        df.to_excel(os.path.join(self._dataset_loc, file_destination))

    def _read_value_from_file(self, file_source, file_row, file_column):
        df = pd.read_excel(os.path.join(self._dataset_loc, file_source), index_col=0, dtype=str).fillna("")
        return df.at[file_row, file_column]

    def _save_widget_info_to_file(self, owner, attr, method, index=1):
        widget = getattr(owner, attr)
        file_destination, file_row, file_column = _determine_location(attr, index)
        value_getter = getattr(widget, method)
        value = value_getter().toString() if attr.startswith("calendarWidget") else value_getter()
        self._save_value_to_file(file_destination, file_row, file_column, value)

    def _save_chips_to_file(self, owner, attr):
        widget = getattr(owner, attr)
        entry_count = self._determine_entry_count(attr)
        texts = _widget_chip_texts(widget)
        for index, text in enumerate(texts):
            file_destination, file_row, file_column = _determine_location(attr, index + 1)
            self._save_value_to_file(file_destination, file_row, file_column, text)

        for index in range(len(texts), entry_count):
            file_destination, file_row, file_column = _determine_location(attr, index + 1)
            self._save_value_to_file(file_destination, file_row, file_column, "")

    def _load_widget_info_from_file(self, owner, attr, method, index=1):
        widget = getattr(owner, attr)
        file_source, file_row, file_column = _determine_location(attr, index)
        value_setter = getattr(widget, method)
        value = self._read_value_from_file(file_source, file_row, file_column)
        value_setter(QtCore.QDate.fromString(value)) if attr.startswith("calendarWidget") else value_setter(value)

    def _load_chips_from_file(self, owner, attr):
        widget = getattr(owner, attr)
        index = 1
        while index:
            try:
                file_source, file_row, file_column = _determine_location(attr, index)
                value = self._read_value_from_file(file_source, file_row, file_column)
                if value:
                    self._add_keyword(value, widget)
                    index += 1
                else:
                    index = 0
            except KeyError:
                index = 0

    def _determine_contributor_count(self):
        tmp_widget = ContributorInformationWidget()
        index = 0

        self._load_widget_info_from_file(tmp_widget.ui_owner(), "comboBox__dataset_description__Contributor_name", "setCurrentText", index + 1)
        current_name = tmp_widget.current_name()
        while current_name:
            index += 1
            try:
                self._load_widget_info_from_file(tmp_widget.ui_owner(), "comboBox__dataset_description__Contributor_name", "setCurrentText", index + 1)
                current_name = tmp_widget.current_name()
            except KeyError:
                current_name = ""

        tmp_widget.destroy()

        return index

    def _determine_other_count(self):
        tmp_widget = OtherInformationWidget()
        index = 0

        for attr in tmp_widget.ui_elements():
            if attr.startswith("comboBox"):
                self._load_widget_info_from_file(tmp_widget.ui_owner(), attr, "setCurrentText", index + 1)

        while not tmp_widget.is_empty():
            index += 1
            try:
                tmp_widget.destroy()
                tmp_widget = OtherInformationWidget()
                for attr in tmp_widget.ui_elements():
                    if attr.startswith("comboBox"):
                        self._load_widget_info_from_file(tmp_widget.ui_owner(), attr, "setCurrentText", index + 1)
            except KeyError:
                pass

        tmp_widget.destroy()

        return index

    def _determine_entry_count(self, attr):
        index = 1
        while index:
            try:
                file_source, file_row, file_column = _determine_location(attr, index)
                value = self._read_value_from_file(file_source, file_row, file_column)
                if value:
                    index += 1
                else:
                    return index
            except KeyError:
                return index

        return index

    def _load_information(self):
        self._create_manifest()

        for attr in dir(self._ui):
            if attr.startswith("comboBox"):
                self._load_widget_info_from_file(self._ui, attr, "addItem")
            elif attr.startswith("plainTextEdit"):
                self._load_widget_info_from_file(self._ui, attr, "setPlainText")
            elif attr.startswith("calendarWidget"):
                self._load_widget_info_from_file(self._ui, attr, "setSelectedDate")
            elif attr.startswith("spinBox"):
                self._load_widget_info_from_file(self._ui, attr, "valueFromText")
            elif attr.startswith("widgetForChips"):
                self._load_chips_from_file(self._ui, attr)

        contributor_count = self._determine_contributor_count()
        for index in range(contributor_count):
            if index >= self._ui.tabWidgetContributors.count():
                self._add_contributor_information_tab(load_database_info=False)

            widget = self._ui.tabWidgetContributors.widget(index)
            for attr in widget.ui_elements():
                if attr.startswith("comboBox"):
                    self._load_widget_info_from_file(widget.ui_owner(), attr, "addItem", index + 1)

        other_count = self._determine_other_count()
        for index in range(other_count):
            if index >= self._ui.tabWidgetOthers.count():
                self._add_other_information_tab(load_database_info=False)

            widget = self._ui.tabWidgetOthers.widget(index)
            for attr in widget.ui_elements():
                if attr.startswith("comboBox"):
                    self._load_widget_info_from_file(widget.ui_owner(), attr, "addItem", index + 1)

    def _save_information(self):
        self._save_value_to_file("dataset_description.xlsx", "Type", "Value", self._dataset_type)

        for attr in dir(self._ui):
            if attr.startswith("comboBox"):
                self._save_widget_info_to_file(self._ui, attr, "currentText")
            elif attr.startswith("plainTextEdit"):
                self._save_widget_info_to_file(self._ui, attr, "toPlainText")
            elif attr.startswith("calendarWidget"):
                self._save_widget_info_to_file(self._ui, attr, "selectedDate")
            elif attr.startswith("spinBox"):
                self._save_widget_info_to_file(self._ui, attr, "value")
            elif attr.startswith("widgetForChips"):
                self._save_chips_to_file(self._ui, attr)

        for index in range(self._ui.tabWidgetContributors.count()):
            widget = self._ui.tabWidgetContributors.widget(index)
            for attr in widget.ui_elements():
                if attr.startswith("comboBox"):
                    self._save_widget_info_to_file(widget.ui_owner(), attr, "currentText", index + 1)

        contributor_count = self._determine_contributor_count()
        tmp_widget = ContributorInformationWidget()
        for index in range(self._ui.tabWidgetContributors.count(), contributor_count):
            for attr in tmp_widget.ui_elements():
                if attr.startswith("comboBox"):
                    self._save_widget_info_to_file(tmp_widget.ui_owner(), attr, "currentText", index + 1)

        tmp_widget.destroy()

        for index in range(self._ui.tabWidgetOthers.count()):
            widget = self._ui.tabWidgetOthers.widget(index)
            for attr in widget.ui_elements():
                if attr.startswith("comboBox"):
                    self._save_widget_info_to_file(widget.ui_owner(), attr, "currentText", index + 1)

        other_count = self._determine_other_count()
        tmp_widget = OtherInformationWidget()
        for index in range(self._ui.tabWidgetOthers.count(), other_count):
            for attr in tmp_widget.ui_elements():
                if attr.startswith("comboBox"):
                    self._save_widget_info_to_file(tmp_widget.ui_owner(), attr, "currentText", index + 1)

        tmp_widget.destroy()

    def _update_database(self):
        contributor_information = self._database.get("Contributor_information", [])
        for index in range(self._ui.tabWidgetContributors.count()):
            widget = self._ui.tabWidgetContributors.widget(index)
            contributor_info = widget.save_database_contributor_information()
            if contributor_info not in contributor_information:
                contributor_information.append(contributor_info)

        attributes_of_interest = ["comboBox__dataset_description__Contributor_name", "comboBox__dataset_description__Contributor_ORCiD"]
        remove_indices = set()
        for i in range(len(contributor_information)):
            for j in range(i + 1, len(contributor_information)):
                for attr in attributes_of_interest:
                    if contributor_information[i][attr] == contributor_information[j][attr]:
                        remove_indices.add(j)

        for i in reversed(list(remove_indices)):
            del contributor_information[i]

        self._database["Contributor_information"] = contributor_information

        other_information = self._database.get("Other_information", {})
        for index in range(self._ui.tabWidgetOthers.count()):
            widget = self._ui.tabWidgetOthers.widget(index)
            other_info = widget.save_database_other_information()
            for key in other_info:
                if key not in other_information:
                    other_information[key] = []

                if other_info[key] and other_info[key] not in other_information[key]:
                    other_information[key].append(other_info[key])

        for attr in dir(self._ui):
            values = None
            if attr.startswith("comboBox"):
                values = self._database.get(attr, [])
                element = getattr(self._ui, attr)
                if element.currentText() not in values:
                    values.append(element.currentText())

            if attr.startswith("databaseOnlyComboBox"):
                values = self._database.get(attr, [])
                buddy_attr = attr.replace("databaseOnlyComboBox", "widgetForChips")
                widget = getattr(self._ui, buddy_attr)
                texts = _widget_chip_texts(widget)
                values = list(set(texts + values))

            if values:
                self._database[attr] = values

        try:
            with FileLock(self._database_filename + ".lock", 3):
                with open(self._database_filename, "w") as fh:
                    json.dump(self._database, fh)
        except Timeout:
            logger.info("Failed to write updated Generate SDS database.")

    def _update_ui(self):
        self._ui.pushButtonRemoveContributor.setEnabled(self._ui.tabWidgetContributors.count() > 1)
        self._ui.pushButtonRemoveOther.setEnabled(self._ui.tabWidgetOthers.count() > 1)

    def _add_contributor_information_tab(self, checked=False, load_database_info=True):
        new_widget = ContributorInformationWidget(self)
        self._ui.tabWidgetContributors.addTab(new_widget, f"   {self._ui.tabWidgetContributors.count() + 1}   ")
        if load_database_info:
            new_widget.load_database_contributor_information(self._database.get("Contributor_information", []))
            new_widget.clear_current()
            self._ui.tabWidgetContributors.setCurrentWidget(new_widget)

        self._update_ui()

    def _add_other_information_tab(self, checked=False, load_database_info=True):
        new_widget = OtherInformationWidget(self)
        self._ui.tabWidgetOthers.addTab(new_widget, f"   {self._ui.tabWidgetOthers.count() + 1}   ")
        if load_database_info:
            new_widget.load_database_other_information(self._database.get("Other_information", {}))
            new_widget.clear_current()
            self._ui.tabWidgetOthers.setCurrentWidget(new_widget)

        self._update_ui()

    def _remove_contributor_information_tab(self):
        self._ui.tabWidgetContributors.removeTab(self._ui.tabWidgetContributors.currentIndex())
        for index in range(self._ui.tabWidgetContributors.count()):
            self._ui.tabWidgetContributors.setTabText(index, f"   {index + 1}   ")
        self._update_ui()

    def _remove_other_information_tab(self):
        self._ui.tabWidgetOthers.removeTab(self._ui.tabWidgetOthers.currentIndex())
        for index in range(self._ui.tabWidgetOthers.count()):
            self._ui.tabWidgetOthers.setTabText(index, f"   {index + 1}   ")
        self._update_ui()

    def _create_manifest(self):
        manifest_file = os.path.join(self._dataset_loc, "primary", "manifest.xlsx")
        if not os.path.exists(manifest_file):
            default_header = ["filename", "timestamp", "description", "file type", "additional types", "species", "organ"]
            if self._dataset_type == "Scaffold":
                default_data = [SCAFFOLD_INFO_FILE, "", "Information on the organ scaffold in JSON format.", "json", "application/x.vnd.abi.organ-scaffold-info+json", "", ""]
            else:
                default_data = [""] * len(default_header)

            df = pd.DataFrame([default_data], columns=default_header)
            df.to_excel(manifest_file, index=False)

    def register_done_execution(self, callback):
        self._callback = callback

    def _done_button_clicked(self):
        self._save_information()
        self._update_database()

        self._callback()
