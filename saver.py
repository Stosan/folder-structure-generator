import os

class FolderStructureSaver:
    """
    A class used to save the structure of a folder to a text file.

    ...

    Attributes
    ----------
    root_folder : str
        a string representing the path of the root folder
    output_file_path : str
        a string representing the path of the output file

    Methods
    -------
    save_folder_structure():
        Saves the structure of the root folder to the output file.
    traverse_folder(folder_path, file, prefix):
        Recursive helper function to traverse the folder structure.
    """

    def __init__(self, root_folder, output_file_path):
        """
        Parameters
        ----------
        root_folder : str
            The path of the root folder
        output_file_path : str
            The path of the output file
        """
        self.root_folder = root_folder
        self.output_file_path = output_file_path

    def save_folder_structure(self):
        """Saves the structure of the root folder to the output file."""
        with open(self.output_file_path, 'w') as f:
            self.traverse_folder(self.root_folder, f, "")

    def traverse_folder(self, folder_path, file, prefix):
        """
        Recursive helper function to traverse the folder structure.

        Parameters
        ----------
        folder_path : str
            The path of the current folder
        file : file object
            The output file object
        prefix : str
            The prefix string to be added before the folder name
        """
        # Get the base name of the folder
        folder_name = os.path.basename(folder_path)
        # Write the folder name to the file
        file.write(f"{prefix}{folder_name}/\n")

        # Iterate over the items in the folder
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            # If the item is a directory, recursively traverse it
            if os.path.isdir(item_path):
                self.traverse_folder(item_path, file, prefix + "    ")
            # If the item is a file, write its name to the file
            else:
                file.write(f"{prefix}    ├── {item}\n")


# Get the current working directory
current_directory = os.getcwd()

# Specify the root folder path based on the current directory
root_folder = current_directory

# Specify the output file path
output_file_path = 'folder_structure.txt'

# Create a FolderStructureSaver object
saver = FolderStructureSaver(root_folder, output_file_path)

# Save the folder structure to the output file
saver.save_folder_structure()