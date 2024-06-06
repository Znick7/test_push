import os
import shutil
import datetime
import schedule
import time

source_dir = "/Users/Znick/Documents/SCREENSHOTS"
destination_dir = "/Users/Znick/Desktop/Local_Backups"

def copy_folder_to_directory(source, dest):
    today == datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    
    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to:  {dest_dir}")
    except FileExistsError:
        print(f"folder already exists in: {dest}")