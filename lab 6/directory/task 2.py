import os

def check(path):
    #Test existence
    if os.path.exists(path):
        print("exists")

        # Test readability
        if os.access(path, os.R_OK):
            print("readable")
        else:
            print("not readable")

        # Test writability
        if os.access(path, os.W_OK):
            print("writable")
        else:
            print("writable")

        # Test executability
        if os.access(path, os.X_OK):
            print("executable")
        else:
            print("not executable")
    else:
        print("does not exist")

my_path = input("The path: ")
check(my_path)
