GENERATE_SDS_DATABASE_FILENAME = "generate_sds_settings.json"
SCAFFOLD_INFO_FILE = "scaffold_info.json"
SCAFFOLD_SETTINGS_MIME_TYPE = "application/x.vnd.abi.scaffold-settings+json"
ARGON_DOCUMENT_MIME_TYPE = "application/x.vnd.abi.cmlibs-argon-document+json"
DERIVATIVE_FOLDER = {"derivative"}


class RequiredFiles:

    def __init__(self):
        self._files = ["dataset_description.xlsx", "submission.xlsx"]
        self._dirs = ["primary"]

    def files(self):
        return self._files

    def dirs(self):
        return self._dirs

    def resource_dir(self):
        return None


class _ConditionalFiles(RequiredFiles):

    def __init__(self):
        super(_ConditionalFiles, self).__init__()
        self._files.extend(["manifest.xlsx", "README.md", "CHANGES"])


class CodeFiles(_ConditionalFiles):

    def __init__(self):
        super(CodeFiles, self).__init__()
        self._files.extend(["code_description.xlsx", "code_parameters.xlsx"])
        self._dirs.extend(["docs", "code"])

    def resource_dir(self):
        return "code"


class ExperimentFiles(_ConditionalFiles):

    def __init__(self):
        super(ExperimentFiles, self).__init__()
        self._files.extend(["subjects.xlsx", "samples.xlsx", "performances.xlsx", "resources.xlsx"])
        self._dirs.extend(["docs", "protocol", "source"])

    def resource_dir(self):
        return "experiment"


class ScaffoldFiles(RequiredFiles):

    def __init__(self):
        super(ScaffoldFiles, self).__init__()


class ComputationalFiles(_ConditionalFiles):

    def __init__(self):
        super(ComputationalFiles, self).__init__()
        self._files.extend(["subjects.xlsx", "samples.xlsx"])
        self._dirs.extend(["derivative"])


PROTOCOL_LAYOUT = {
    "code": CodeFiles(),
    "experiment": ExperimentFiles(),
    "scaffold": ScaffoldFiles(),
    "computational": ComputationalFiles(),
}
