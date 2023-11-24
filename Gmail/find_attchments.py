
import os
from utils import pdf_dir


def find_files(folder, extension):
    files = []
    for root, dirs, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(extension):
                files.append(os.path.join(root, filename))
    return files

folder_path = pdf_dir
file_extension = '.pdf' 

found_files = find_files(folder_path, file_extension)

if found_files:
    print("Found files:")
    for file in found_files:
        print(file.split(".")[0])
else:
    print("No files found.")