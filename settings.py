import json, os, files

class Save_Load:

    def __init__(self) -> None:
        if not os.path.exists("settings.json"): # if a save does not exist, create one. Otherwise, nothing needs to happen.
            self.save_file = open("settings.json", "x")
            self.save_file.close()
        else:
            pass

    @classmethod
    def to_dict(cls, folder : files.Custom_Folder) -> dict:
        # Convert class items to dictionary | Add onto if needed
        return{
            "main_path" : folder.main_path,
            "folder_name" : folder.folder_name,
            "file_exts" : folder.file_exts,
            "folder_path" : folder.folder_path
        }
    
    @classmethod
    def from_dict(cls, data_item : dict) -> files.Custom_Folder:
        # Convert saved dict into a new class
        return files.Custom_Folder(data_item["main_path"], data_item["folder_name"], data_item["file_exts"])

    @classmethod
    def save_to_file(cls, folders : list) -> None:
        cls.save_file = open("settings.json", "w")
        cls.save_file.write(json.dumps([cls.to_dict(folder) for folder in folders], indent= 4)) # Write each class (custom folder) into a json file for saving
        cls.save_file.close()

    @classmethod
    def load_from_file(cls) -> list:
        cls.save_file = open("settings.json", "r")
        folders_data = json.load(cls.save_file)
        folders = []
        for folder in folders_data:
            folders.append(cls.from_dict(folder)) # Reconstruct the class from the information provided in the dict
        cls.save_file.close()
        return folders