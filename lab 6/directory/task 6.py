import os

def generate_text():
    for x in range(ord('A'), ord('Z') + 1):
        file_name = f"{chr(x)}.txt"
        with open(file_name, 'w') as file:
            file.write(f"This file's name is '{file_name}'")

generate_text()

