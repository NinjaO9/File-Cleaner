import pathlib, os, json
import files, settings

prog_sav = settings.Save_Load()

dedicated_path = input("Type the path that you want to clean: \n").replace('"','') # copying path on windows includes quotation marks, so I am removing them

image_extensions = ["jpg", "png", "avif", "jpeg" ]

m360_extensions = ["docx", "pptx", "csv"]

images = files.Custom_Folder(dedicated_path, "images", image_extensions)

pdfs = files.Custom_Folder(dedicated_path, "pdfs", "pdf")

m360 = files.Custom_Folder(dedicated_path, "360", m360_extensions)

executable = files.Custom_Folder(dedicated_path, "executables", "exe")

custom_folders = [images, pdfs, m360, executable] 

#custom_folders = prog_sav.load_from_file()

directories = pathlib.Path(dedicated_path).iterdir()

for item in list(directories):
    item = str(item).replace(dedicated_path, '')
    extention = str((item.split('.'))[-1]) # get the extention on its own using split()
    print(extention)
    for folder in custom_folders:
        if extention in folder.file_exts:
            os.rename(dedicated_path + item, folder["folder_path"] + item)

#prog_sav.save_to_file(custom_folders)


        