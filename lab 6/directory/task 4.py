def sum_lines(file_path):

    with open(file_path, 'r') as file:
        line_count = sum(1 for line in file)
        print(f"{line_count} lines")

import os
file_path = input("The text file: ")
sum_lines(file_path)
