import os


def save_folder_structure(root_path, output_file):
    with open(output_file, 'w') as f:
        traverse_folder(root_path, f, "")

def traverse_folder(folder_path, file, prefix):
    folder_name = os.path.basename(folder_path)
    file.write(f"{prefix}{folder_name}/\n")

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            traverse_folder(item_path, file, prefix + "    ")
        else:
            file.write(f"{prefix}    ├── {item}\n")

# Get the current working directory
current_directory = os.getcwd()

# Specify the root folder path based on the current directory
root_folder = current_directory

# Specify the output file path
output_file_path = 'folder_structure.txt'

# Save the folder structure to the output file
save_folder_structure(root_folder, output_file_path)
