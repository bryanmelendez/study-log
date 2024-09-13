import yaml


class Settings:
    def __init__(self):
        self.subjects = list()
        self.save_path = None
        self.goal = None
        self.settings_file = "settings.yaml"

    # Read from settings.yaml

    def get_settings(self):
        settings = dict()

        with open(self.settings_file, "r") as infile:
            settings = yaml.safe_load(infile)

        self.subjects = settings["subjects"]
