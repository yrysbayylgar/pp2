import os

def delete_file(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        print("File not found.")
        return
    
    else: # Delete the file
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")


my_path = input("The file path to delete: ")
delete_file(my_path)
