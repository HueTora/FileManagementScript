import os
import shutil


folders = {
    ".blend": "blend_files",
    ".fbx": "models",
    ".jpg": "images",
    ".png": "images",
    ".gif": "gifs"
}

values = list(folders.values())
keys = list(folders.keys())

path = r"C:\Users\Workming\Pictures\test_dir"
with os.scandir(path) as files:
    files = [file.name for file in files]
    for key in folders:
        value = folders[key]
        if value not in files:
            os.mkdir(path + f"\\{value}")
            print(value, "folder created")


with os.scandir(path) as files:
    for file in files:
        file_name, file_extension = os.path.splitext(file)
        if file_extension in folders:
            dest_folder = values[keys.index(file_extension)]
            src = path + f"\\{file.name}"
            dest = path + f"\\{dest_folder}\\{file.name}"
            shutil.move(src, dest)


