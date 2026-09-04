import os
import shutil

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("❌ The specified folder does not exist!")
        return

    # Dictionary to map extensions to folder names
    extension_folders = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Music': ['.mp3', '.wav', '.flac'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Others': []  # will store files with other extensions
    }

    # Create subfolders
    for folder in extension_folders.keys():
        os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

    # Organize files
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file_name)
            ext = ext.lower()

            moved = False
            for folder, extensions in extension_folders.items():
                if ext in extensions:
                    shutil.move(file_path, os.path.join(folder_path, folder, file_name))
                    moved = True
                    break

            if not moved:
                shutil.move(file_path, os.path.join(folder_path, 'Others', file_name))

if __name__ == "__main__":
    path = input("Enter the folder path to organize: ").strip()
    organize_files(path)
