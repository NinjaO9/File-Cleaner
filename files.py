import os, pathlib

class Custom_Folder:

    def __init__(self, dedicated_path : str, folder_name : str, file_extensions : list) -> None:
        self.main_path = dedicated_path
        self.folder_name = folder_name
        self.file_exts = file_extensions
        self.folder_path = self.main_path + self.folder_name # The reason I am making these into seperate values (dedicated path and folder name) is just incase I was more customizability between values

        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def change_folder_name(self) -> None:
        satisfied = False
        while not satisfied:
            new_name = str(input("What would you like to rename your folder to?\n"))

            if (new_name[0] != '\\'): #formatting
                new_name = "\\" + new_name
            if (os.path.exists(self.main_path + new_name) and new_name != self.folder_name): # check for discrepensies
                choice = str(input(f"WARNING: path '{self.main_path + new_name}' already exists! Writing into this folder could cause unwanted actions. Are you sure you want to use this folder? (Y/N)\n"))
            else:
                choice = str(input(f"Are you satisfied with the name '{new_name[1:]}'? (Y/N)\n"))

            if (choice.upper() == "Y"):
                satisfied = True
        self.transfer_files(new_name)
        os.removedirs(self.folder_path)
        self.folder_name = new_name
        self.folder_path = self.main_path + self.folder_name
        
    def transfer_files(self, new_folder : str) -> None:
        if not (os.path.exists(self.main_path + new_folder)):
            os.makedirs(self.main_path + new_folder)
        
        for item in list(pathlib.Path(self.folder_path).iterdir()):
            item = str(item).replace(self.folder_path, '') #get the item alone
            os.rename((self.folder_path + item), ((self.main_path + new_folder) + item))

    def add_extention(self, extention : str) -> None:
        if extention in self.file_exts:
            print(f"The extention {extention} already exists!")
        else:
            self.file_exts.append(extention)

    def remove_extention(self, extention : str) -> None:
        try:
            self.file_exts.remove(extention)
        except ValueError as e:
            print(f"Argument {extention} was not found in the current list of extentions!")


class Folder_Actions:

    def __init__(self):
        pass

    @classmethod
    def get_dedicated_path(cls) -> None: 
        dedicated_path = input("Type a valid path that you want to clean (e.g. 'C:\\Users\\Ninja09\\Downloads'): \n").replace('"','') # copying path on windows includes quotation marks, so I am removing them
        if os.path.exists(dedicated_path):
            return dedicated_path
        else:
            print(f"Path '{dedicated_path}' was not found!")
            cls.get_dedicated_path() # Prompt again for a path, until a proper path is given

    @classmethod
    def clean_dir(cls, dedicated_path : str, custom_folders : list) -> None: 
        # sort/clean the directory that was given from the dedicated_path
        directories = pathlib.Path(dedicated_path).iterdir()
        for item in list(directories):
            item = str(item).replace(dedicated_path, '')
            extention = str((item.split('.'))[-1]) # get the extention on its own using split()
            print(extention) # Debug print
            for folder in custom_folders:
                if extention in folder.file_exts:
                    os.rename(dedicated_path + item, folder.folder_path + item)

    @classmethod
    def edit_folders(cls, custom_folders : list) -> None:
        file_num = 0
        choice = -1
        # list custom_folder and allow user to select what folder presets they want to edit
        print("Which preset would you like to edit?\n")
        for folder in custom_folders:
            file_num += 1
            print(f"{file_num}: {folder.folder_name}")
        while choice > file_num or choice < 0:
            choice = int(input(" "))  
        file_num = (choice - 1) # repurposing file_num to hold the index of the folder that was selected

        match (cls.select_action()):
            case 1:
                custom_folders[file_num].change_folder_name()
            case 2:
                custom_folders[file_num].add_extention(str(input("Type the extention you would like to add (exclude the '.')")))
            case 3:
                custom_folders[file_num].remove_extention(str(input("Type the extention you would like to remove (exclude the '.')")))
        
        
    @classmethod
    def select_action(cls) -> int:
        choice = int(input("""
What would you like to do?
1) Change folder name
2) Add extention
3) Remove extention
                           """))
        if choice < 1 or choice > 3: # Restart selection of choice if  'choice' doesnt match any of the allowed inputs (1-3)
            choice = cls.select_action()
        
        return choice
    
    @classmethod
    def create_cf(cls, main_path) -> Custom_Folder:
        extentions = []
        name = ''

        while (True): # Don't create duplicate instances of a folder
            name = str(input("Enter a name for the custom folder: "))
            if (os.path.exists(main_path + name)):
                print("ERROR: Folder already exists!")
            elif (str(input(f"(Y/N) Are you happy with the name: {name}?\n").upper() == 'y')):
                break

        if (name[0] != "\\"): # Formatting
            name = "\\" + name
        
        extention = str(input("Enter extentions to add to this custom folder (Type 'Done' to exit): "))
        while (extention.upper() != "DONE"):
            extentions.append(extention)
            extention = str(input("Enter extentions to add to this custom folder (Type 'Done' to exit): "))
        
        new_folder = Custom_Folder(main_path, name, extentions)


        return new_folder
    
    @classmethod
    def verify_newfolder(cls, nfolder : Custom_Folder) -> int:
                print(f"""
NEW FOLDER:
    -PATH {nfolder.folder_path}
    -NAME {nfolder.folder_name}
    -ENTENTIONS {nfolder.file_exts}              
""")
                if (str(input("Are you happy with your choices?(Y/N): ")).upper() == 'Y'):
                    return 1
                return 0    