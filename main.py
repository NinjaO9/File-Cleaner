import pathlib, os

dedicated_path = input("Type the path that you want to clean: \n").replace('"','') # copying path on windows includes quotation marks, so I am removing them

image_extensions = [".jpg", ".png", "avif", "jpeg" ]

m360_extensions = ["docx", "pptx", ".csv"]

if not (os.path.exists(dedicated_path + r"\images")): # Creating folders to sort items into. Gonna make this into classes and stuff probably for better customizability
    os.makedirs(dedicated_path + r"\images")

if not (os.path.exists(dedicated_path + r"\pdfs")):
    os.makedirs(dedicated_path + r"\pdfs")
    
if not (os.path.exists(dedicated_path + r"\360")):
    os.makedirs(dedicated_path + r"\360")

if not (os.path.exists(dedicated_path + r"\executables")):
    os.makedirs(dedicated_path + r"\executables")

for item in list(pathlib.Path(dedicated_path).iterdir()):
    print(f"{str(item)[-4:]}")
    if (str(item)[-4:] in image_extensions):
        #print("FILE FOUUUNDDDDDDDDDDDD\n")
        item = str(item).replace(dedicated_path, '')
        #print(folder_path + item)
        os.rename(dedicated_path + item, (dedicated_path + r"\images") + item)
    elif (str(item)[-4:] == ".pdf"):
        item = str(item).replace(dedicated_path, '')
        os.rename(dedicated_path + item, (dedicated_path + r"\pdfs") + item)
    elif (str(item)[-4:] in m360_extensions):
        item = str(item).replace(dedicated_path, '')
        os.rename(dedicated_path + item, (dedicated_path + r"\360") + item)
    elif (str(item)[-4:] == ".exe"):
        item = str(item).replace(dedicated_path, '')
        os.rename(dedicated_path + item, (dedicated_path + r"\executables") + item)

        