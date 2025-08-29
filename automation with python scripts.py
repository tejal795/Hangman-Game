import os
import shutil

def move_jpg_files(source_folder, destination_folder):
    # Check if source and destination folders exist
    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist.")
        return
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Destination folder '{destination_folder}' created.")

    # Move .jpg files from source to destination folder
    jpg_files = [file for file in os.listdir(source_folder) if file.endswith('.jpg')]
    for file in jpg_files:
        source_file_path = os.path.join(source_folder, file)
        destination_file_path = os.path.join(destination_folder, file)
        shutil.move(source_file_path, destination_file_path)
        print(f"Moved '{file}' to '{destination_folder}'")

    print(f"Moved {len(jpg_files)} .jpg files from '{source_folder}' to '{destination_folder}'")

def main():
    source_folder = input("Enter the source folder path: ")
    destination_folder = input("Enter the destination folder path: ")
    move_jpg_files(source_folder, destination_folder)

if _name_ == "_main_":
    main()