import pandas as pd
import os
import os
import shutil

def duplicate_folder_with_renaming(source_folder, dest_folder, df : pd.DataFrame):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    count = 1
    df_idx = 0
    for df_idx, expected_file in enumerate(df['path']):
        images = set(os.listdir(source_folder))
        print(expected_file in images)
        if expected_file in images:

            #Save imge to the new folder
            source_path = os.path.join(source_folder, expected_file)
            dest_path = os.path.join(dest_folder, f"LoremIpsum ({count}).png")
            shutil.copy2(source_path, dest_path)

            #Save text to the new folder
            text_dir = 'training_desriptions'
            if not os.path.exists(text_dir):
                os.makedirs(text_dir)

            filename = f"LoremIpsum ({count}).txt"
            file_content = df['description'][df_idx]
            text_file_path = os.path.join(text_dir, filename)
            with open(text_file_path, 'w') as file:
                file.write(file_content)
            count += 1
            
    print(f"Folder '{source_folder}' duplicated to '{dest_folder}' with renamed files.")

if __name__ == "__main__":
    df = pd.read_csv(r'C:\Users\Eli Brignac\Downloads\Destiny_Weapon_Maker\Descriptions\image_descriptions.csv')
    source_folder = r"C:\Users\Eli Brignac\Downloads\Destiny_Weapon_Maker\Descriptions\images"
    dest_folder = r"C:\Users\Eli Brignac\Downloads\Destiny_Weapon_Maker\Descriptions\training_images"
    duplicate_folder_with_renaming(source_folder, dest_folder, df)
    

print("Text files created successfully!")
