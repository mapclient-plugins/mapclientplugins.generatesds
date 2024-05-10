import json
import logging

import os.path
import pandas as pd

from PySide6 import QtCore, QtWidgets
from filelock import FileLock, Timeout
from mapclient.settings.general import get_data_directory
from mapclientplugins.generatesdsstep.contributorinformationwidget import ContributorInformationWidget
from mapclientplugins.generatesdsstep.definitions import GENERATE_SDS_DATABASE_FILENAME, SCAFFOLD_INFO_FILE
from mapclientplugins.generatesdsstep.ui_generatesdswidget import Ui_GenerateSDSWidget

logger = logging.getLogger(__name__)


def _determine_destination(text, index):
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


class GenerateSDSWidget(QtWidgets.QWidget):

    def __init__(self, dataset_loc, dataset_type, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self._ui = Ui_GenerateSDSWidget()
        self._ui.setupUi(self)
        self._ui.groupBoxManifest.setVisible(dataset_type == "Scaffold")
        self._add_contributor_information_tab()

        application_data_directory = get_data_directory()
        self._database = {}
        self._database_filename = os.path.join(application_data_directory, GENERATE_SDS_DATABASE_FILENAME)

        self._dataset_loc = dataset_loc
        self._dataset_type = dataset_type

        self._load_database()
        self._load_information()

        self._make_connections()
        self._callback = None

    def _make_connections(self):
        self._ui.pushButtonDone.clicked.connect(self._done_button_clicked)
        self._ui.pushButtonAddContributor.clicked.connect(self._add_contributor_information_tab)
        self._ui.pushButtonRemoveContributor.clicked.connect(self._remove_contributor_information_tab)

    def _load_database(self):
        if os.path.isfile(self._database_filename):
            try:
                with FileLock(self._database_filename + ".lock", 3):
                    with open(self._database_filename) as fh:
                        self._database = json.load(fh)
            except Timeout:
                logger.info("Failed to read Generate SDS database.")

    def _save_value_to_file(self, file_destination, file_row, file_column, value):
        df = pd.read_excel(os.path.join(self._dataset_loc, file_destination), index_col=0).fillna("")
        df.at[file_row, file_column] = value
        df.to_excel(os.path.join(self._dataset_loc, file_destination))

    def _read_value_from_file(self, file_source, file_row, file_column):
        df = pd.read_excel(os.path.join(self._dataset_loc, file_source), index_col=0).fillna("")
        return df.at[file_row, file_column]

    def _save_widget_info_to_file(self, owner, attr, method, index=1):
        widget = getattr(owner, attr)
        file_destination, file_row, file_column = _determine_destination(attr, index)
        value_getter = getattr(widget, method)
        value = value_getter().toString() if attr.startswith("calendarWidget") else value_getter()
        self._save_value_to_file(file_destination, file_row, file_column, value)

    def _load_widget_info_from_file(self, owner, attr, method, index=1):
        widget = getattr(owner, attr)
        file_source, file_row, file_column = _determine_destination(attr, index)
        value_setter = getattr(widget, method)
        value = self._read_value_from_file(file_source, file_row, file_column)
        value_setter(QtCore.QDate.fromString(value)) if attr.startswith("calendarWidget") else value_setter(value)

    def _determine_contributor_count(self):
        widget = self._ui.tabWidgetContributors.widget(0)
        index = 0

        self._load_widget_info_from_file(widget.ui_owner(), "comboBox__dataset_description__Contributor_name", "setCurrentText", index + 1)
        current_name = widget.current_name()
        while current_name:
            index += 1
            try:
                self._load_widget_info_from_file(widget.ui_owner(), "comboBox__dataset_description__Contributor_name", "setCurrentText", index + 1)
                current_name = widget.current_name()
            except KeyError:
                current_name = ""

        return index

    def _load_information(self):
        self._create_manifest()

        for attr in dir(self._ui):
            if attr.startswith("comboBox"):
                self._load_widget_info_from_file(self._ui, attr, "setCurrentText")
            elif attr.startswith("plainTextEdit"):
                self._load_widget_info_from_file(self._ui, attr, "setPlainText")
            elif attr.startswith("calendarWidget"):
                self._load_widget_info_from_file(self._ui, attr, "setSelectedDate")

        contributor_count = self._determine_contributor_count()
        for index in range(contributor_count):
            if index >= self._ui.tabWidgetContributors.count():
                self._add_contributor_information_tab()

            self._load_widget_info_from_file(self._ui.tabWidgetContributors.widget(index).ui_owner(), "comboBox__dataset_description__Contributor_name", "setCurrentText", index + 1)

    def _save_information(self):
        self._save_value_to_file("dataset_description.xlsx", "Type", "Value", self._dataset_type)

        for attr in dir(self._ui):
            if attr.startswith("comboBox"):
                self._save_widget_info_to_file(self._ui, attr, "currentText")
            elif attr.startswith("plainTextEdit"):
                self._save_widget_info_to_file(self._ui, attr, "toPlainText")
            elif attr.startswith("calendarWidget"):
                self._save_widget_info_to_file(self._ui, attr, "selectedDate")

        for index in range(self._ui.tabWidgetContributors.count()):
            widget = self._ui.tabWidgetContributors.widget(index)
            for attr in widget.ui_elements():
                if attr.startswith("comboBox"):
                    self._save_widget_info_to_file(widget.ui_owner(), attr, "currentText", index + 1)

        contributor_count = self._determine_contributor_count()
        tmp_widget = ContributorInformationWidget(self)
        for index in range(self._ui.tabWidgetContributors.count(), contributor_count):
            for attr in tmp_widget.ui_elements():
                if attr.startswith("comboBox"):
                    self._save_widget_info_to_file(tmp_widget.ui_owner(), attr, "currentText", index + 1)

    def _update_database(self):
        try:
            with FileLock(self._database_filename + ".lock", 3):
                with open(self._database_filename, "w") as fh:
                    json.dump(self._database, fh)
        except Timeout:
            logger.info("Failed to write updated Generate SDS database.")

    def _update_ui(self):
        self._ui.pushButtonRemoveContributor.setEnabled(self._ui.tabWidgetContributors.count() > 1)

    def _add_contributor_information_tab(self):
        new_widget = ContributorInformationWidget(self)
        self._ui.tabWidgetContributors.addTab(new_widget, f"   {self._ui.tabWidgetContributors.count() + 1}   ")
        self._update_ui()

    def _remove_contributor_information_tab(self):
        self._ui.tabWidgetContributors.removeTab(self._ui.tabWidgetContributors.currentIndex())
        for index in range(self._ui.tabWidgetContributors.count()):
            self._ui.tabWidgetContributors.setTabText(index, f"   {index + 1}   ")
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
