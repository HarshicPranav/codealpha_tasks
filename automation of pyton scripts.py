import os
import shutil


DOWNLOADS_FOLDER = "C:/Users/YourUsername/Downloads"  
ORGANIZED_FOLDER = "C:/Users/YourUsername/OrganizedDownloads"  


FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".java", ".c", ".cpp", ".js", ".html", ".css"],
    "Others": []  
}


def organize_files():
    
    for category in FILE_CATEGORIES:
        folder_path = os.path.join(ORGANIZED_FOLDER, category)
        os.makedirs(folder_path, exist_ok=True)

    
    for filename in os.listdir(DOWNLOADS_FOLDER):
        file_path = os.path.join(DOWNLOADS_FOLDER, filename)

        
        if os.path.isdir(file_path):
            continue

        
        file_extension = os.path.splitext(filename)[1].lower()
        category_found = False

        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                destination_folder = os.path.join(ORGANIZED_FOLDER, category)
                shutil.move(file_path, destination_folder)
                print(f"Moved '{filename}' to '{category}'")
                category_found = True
                break

        
        if not category_found:
            destination_folder = os.path.join(ORGANIZED_FOLDER, "Others")
            shutil.move(file_path, destination_folder)
            print(f"Moved '{filename}' to 'Others'")

    print("\nFile organization complete!")

# Run the script
if __name__ == "__main__":
    organize_files()
