import os

def check_info(path):
    if os.path.exists(path):
        print("exists")

        directory = os.path.dirname(path)
        filename = os.path.basename(path)

        print(f"Directory: {directory}")
        print(f"Filename: {filename}")
    else:
        print("The path does not exist.")

my_path = input("The path: ")
check_info(my_path)
