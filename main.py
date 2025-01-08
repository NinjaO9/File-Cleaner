import files, settings

def main():
    prog_sav = settings.Save_Load()

    print("Loading saved folder presets...")
    custom_folders = prog_sav.load_from_file()
    dedicated_path = files.Folder_Actions.get_dedicated_path()
    while True:
        print("What would you like to do?")
        choice = int(input("""
        1) Sort Files
        2) Change dedicated directory
        3) Edit File Configs
        4) Add Custom File Config
                           """))
        match choice:
            case 1:
                files.Folder_Actions.clean_dir(dedicated_path, custom_folders)
            case 2:
                dedicated_path = files.Folder_Actions.get_dedicated_path()
            case 3:
                files.Folder_Actions.edit_folders(custom_folders)
            case 4:
                pass
            case 5:
                pass
        print("Saving current folder presets...")
        prog_sav.save_to_file(custom_folders)

main()