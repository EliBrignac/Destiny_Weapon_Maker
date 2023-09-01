import os
import shutil

def duplicate_folder_with_renaming(source_folder, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    count = 1
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            source_path = os.path.join(root, file)
            dest_path = os.path.join(dest_folder, f"Img ({count}).png")
            count += 1
            shutil.copy2(source_path, dest_path)
    
    print(f"Folder '{source_folder}' duplicated to '{dest_folder}' with renamed files.")

if __name__ == "__main__":
    source_folder = r"C:\Users\Eli Brignac\Downloads\Destiny_Weapon_Maker\Destiny_Weapon_Maker\readme_images"
    dest_folder = r"C:\Users\Eli Brignac\Downloads\Destiny_Weapon_Maker\Destiny_Weapon_Maker\readme_imgs"
    duplicate_folder_with_renaming(source_folder, dest_folder)
