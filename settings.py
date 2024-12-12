import json, os

class Save_Load:

    def __init__(self) -> None:
        if not os.path.exists("settings.json"): # if a save does not exist, create one. Otherwise, nothing needs to happen.
            self.save_file = open("settings.json", "x")
            self.save_file.close()
        else:
            pass

    def save_to_file(self, folders : list) -> None:
        self.save_file = open("settings.json", "w")
        self.save_file.write(json.dumps([folder.__dict__ for folder in folders]))
        self.save_file.close()

    def load_from_file(self) -> list:
        self.save_file = open("settings.json", "r")
        folders = json.load(self.save_file)
        return folders
