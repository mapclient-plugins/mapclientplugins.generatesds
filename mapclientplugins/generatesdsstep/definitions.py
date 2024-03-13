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


class CodeFiles(RequiredFiles):

    def __init__(self):
        super(CodeFiles, self).__init__()
        self._files.extend(["code_description.xlsx", "code_parameters.xlsx", "manifest.xlsx", "README.txt", "CHANGES.txt"])
        self._dirs.extend(["docs", "code"])

    def resource_dir(self):
        return "code"


class ExperimentFiles(RequiredFiles):

    def __init__(self):
        super(ExperimentFiles, self).__init__()
        self._files.extend(["subjects.xlsx", "samples.xlsx", "performances.xlsx", "resources.xlsx", "manifest.xlsx", "README.txt", "CHANGES.txt"])
        self._dirs.extend(["docs", "protocol", "source"])

    def resource_dir(self):
        return "experiment"


class ScaffoldFiles(RequiredFiles):

    def __init__(self):
        super(ScaffoldFiles, self).__init__()


PROTOCOL_LAYOUT = {
    "Code": CodeFiles(),
    "Experiment": ExperimentFiles(),
    "Scaffold": ScaffoldFiles(),
}
