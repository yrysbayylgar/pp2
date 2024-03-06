import os

def list_directories(path):
    print("Directories:")
    for entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, entry)):
            print(entry)

def list_files(path):
    print("\nFiles:")
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            print(entry)

def list_all_items(path):
    print("\nAll Directories and Files:")
    for entry in os.listdir(path):
        print(entry)


a_path = input("your path: ")

if os.path.exists(a_path):
    list_directories(a_path)
    list_files(a_path)
    list_all_items(a_path)
else:
    print("Invalid path")
