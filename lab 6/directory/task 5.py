def list_to_file(file_path, my_list):
    
    file = open(file_path, 'w')

    for item in my_list:
        file.write(str(item) + '\n')

    file.close()
    print("The list has been written")

file_path = input("The path: ")
my_list = input("The list elements(use comma): ").split(',')

list_to_file(file_path, my_list)
