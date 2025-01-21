from json import JSONDecodeError
import files, settings

def main():
    prog_sav = settings.Save_Load()

    try:
        custom_folders = prog_sav.load_from_file()
        print("Loaded saved folder presets")
    except JSONDecodeError as error:
        custom_folders = []
        
    dedicated_path = files.Folder_Actions.get_dedicated_path()
    while True:
        print("What would you like to do?")
        choice = int(input("""
        1) Sort Files
        2) Change dedicated directory
        3) Edit File Configs
        4) Add Custom File Config
        5) Exit
                           """))
        match choice:
            case 1:
                files.Folder_Actions.clean_dir(dedicated_path, custom_folders)
            case 2:
                dedicated_path = files.Folder_Actions.get_dedicated_path()
            case 3:
                files.Folder_Actions.edit_folders(custom_folders)
            case 4:
                new_file = files.Folder_Actions.create_cf(dedicated_path)
                if (files.Folder_Actions.verify_newfolder(new_file)):
                    custom_folders.append(new_file)
                    print(f"New folder {new_file.folder_name} saved!")
                else:
                    print("New folder not saved")
                new_file = None
            case 5:
                print("Exiting...")
                break
        print("Saving current folder presets...")
        prog_sav.save_to_file(custom_folders)

main()