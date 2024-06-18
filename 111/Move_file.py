import os
import shutil

from_dir = "C:/Users/admin/Downloads"
to_dir = "C:/Users/admin/Documents/Document_Files"

shutil.move(from_dir,to_dir)

list_of_files = os.listdir(from_dir)
print(list_of_files)