import os
import shutil

def organize_folder(target_directory):
    # Define the mapping for file categories based on extensions
    EXTENSIONS_MAPPING = {
        'Documents': ['.txt', '.pdf', '.docx', '.xlsx', '.pptx', '.md'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.bmp'],
        'Scripts': ['.py', '.js', '.html', '.css', '.java', '.cpp'],
        'Archives': ['.zip', '.tar', '.rar', '.gz']
    }

    print(f"Starting to organize files in: {target_directory}")

    # Check if target directory exists
    if not os.path.exists(target_directory):
        print("Error: The specified folder does not exist.")
        return

    # Scan all files in the directory
    for filename in os.listdir(target_directory):
        file_path = os.path.join(target_directory, filename)

        # Skip folders, only look at files
        if os.path.isdir(file_path):
            continue

        # Find the file extension
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()

        # Find the correct destination folder
        destination_folder = 'Others'
        for folder_name, extensions in EXTENSIONS_MAPPING.items():
            if file_extension in extensions:
                destination_folder = folder_name
                break

        # Create the folder path if it doesn't exist yet
        folder_path = os.path.join(target_directory, destination_folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Securely move the file into its new folder
        shutil.move(file_path, os.path.join(folder_path, filename))
        print(f"Successfully moved: {filename} -> {destination_folder}/")

    print("Folder organization complete! Everything is perfectly neat.")

# Example usage (Can be targeted to a cluttered project directory)
if __name__ == "__main__":
    # Using a placeholder directory that can be updated by the system administrator
    current_working_dir = os.getcwd()
    organize_folder(current_working_dir)
          
