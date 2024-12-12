import os, pathlib

class Custom_Folder:

    def __init__(self, dedicated_path : str, folder_name : str, file_extensions : list) -> None:
        self.main_path = dedicated_path
        self.folder_name =  "\\" + folder_name #TODO: ensure that "folder name" doesn't have a backslash character in the first character of the string
        self.file_exts = file_extensions
        self.folder_path = self.main_path + self.folder_name # The reason I am making these into seperate values (dedicated path and folder name) is just incase I was more customizability between values

        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def change_folder_name(self) -> None:
        while True:
            new_name = str(input("What would you like to rename your folder to?\n"))
            if (new_name[0] != '\\'): #formatting
                new_name = "\\" + new_name
            if (os.path.exists(self.main_path + new_name) and new_name != self.folder_name): # check for discrepensies
                choice = str(input(f"WARNING: path '{self.main_path + new_name}' already exists! Writing into this folder could cause unwanted actions. Are you sure you want to use this folder? (Y/N)\n"))
                if (choice.upper() == "Y"):
                    break
            else:
                choice = str(input(f"Are you satisfied with the name '{new_name[1:]}'? (Y/N)\n"))
                if (choice.upper == 'Y'):
                    break
        self.transfer_files(self, new_name)
        os.removedirs(self.folder_path)
        self.folder_name = new_name
        self.folder_path = self.main_path + self.folder_name
        
    def transfer_files(self, new_folder : str) -> None:
        if not (os.path.exists(self.main_path + new_folder)):
            os.makedirs(self.main_path + new_folder)
        
        for item in list(pathlib.Path(self.main_path).iterdir()):
            str(item).replace(self.folder_path, '') #get the item alone
            os.rename(self.folder_path + item, (self.main_path + new_folder) + item)

    def add_extention(self, extention : str) -> None:
        if extention in self.file_exts:
            print(f"The extention {extention} already exists!")
        else:
            self.file_exts.append('.' + extention)

    def remove_extention(self, extention : str) -> None:
        try:
            self.file_exts.remove(extention)
        except ValueError as e:
            print(f"Argument {extention} was not found in the current list of extentions!")
    