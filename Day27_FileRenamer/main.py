import os

def rename_files(folder_path, new_name):
    if not os.path.exists(folder_path):
        print("❌ The specified folder does not exist!")
        return

    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    files.sort()  # Sort files for consistent order

    count = 1
    for file_name in files:
        old_path = os.path.join(folder_path, file_name)
        name, ext = os.path.splitext(file_name)
        new_file_name = f"{new_name}_{count}{ext}"
        new_path = os.path.join(folder_path, new_file_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {file_name} -> {new_file_name}")
        count += 1

    print("\n✅ All files renamed successfully!")

if __name__ == "__main__":
    path = input("Enter the folder path: ").strip()
    new_name = input("Enter new base name (e.g., file): ").strip()
    rename_files(path, new_name)
