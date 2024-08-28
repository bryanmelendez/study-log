import json


class Settings:
    def __init__(self):
        self.subjects = list()
        self.save_path = None
        self.goal = None

    # Read from settings.json
