import pathlib, os, json
import files, settings

prog_sav = settings.Save_Load()

dedicated_path = input("Type the path that you want to clean: \n").replace('"','') # copying path on windows includes quotation marks, so I am removing them

custom_folders = prog_sav.load_from_file()

directories = pathlib.Path(dedicated_path).iterdir()

for item in list(directories):
    item = str(item).replace(dedicated_path, '')
    extention = str((item.split('.'))[-1]) # get the extention on its own using split()
    print(extention)
    for folder in custom_folders:
        if extention in folder.file_exts:
            os.rename(dedicated_path + item, folder.folder_path + item)

prog_sav.save_to_file(custom_folders)