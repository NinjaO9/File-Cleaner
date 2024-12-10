import pathlib, os
import files



dedicated_path = input("Type the path that you want to clean: \n").replace('"','') # copying path on windows includes quotation marks, so I am removing them

image_extensions = [".jpg", ".png", "avif", "jpeg" ]

m360_extensions = ["docx", "pptx", ".csv"]

images = files.Custom_Folder(dedicated_path, r"\images", image_extensions)

pdfs = files.Custom_Folder(dedicated_path, r"\pdfs", ".pdf")

m360 = files.Custom_Folder(dedicated_path, r"\360", m360_extensions)

executable = files.Custom_Folder(dedicated_path, r"\executables", ".exe")

custom_folders = [images, pdfs, m360, executable]

for item in list(pathlib.Path(dedicated_path).iterdir()):
    print(f"{str(item)[-4:]}")
    item = str(item).replace(dedicated_path, '')
    for folder in custom_folders:
        if item[-4:] in folder.file_exts:
            os.rename(dedicated_path + item, folder.folder_path + item)


        