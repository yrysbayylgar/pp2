def copy_file(source_path, destination_path):

    with open(source_path, 'r') as source_file:
        content = source_file.read()
        
    with open(destination_path, 'w') as destination_file:
        destination_file.write(content)

import os
source = input("The source file path: ")
destination = input("The destination file path: ")

copy_file(source, destination)
