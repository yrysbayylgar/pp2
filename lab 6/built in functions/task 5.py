def all_true(t):
    return all(t)

elements_input = input()
user_tuple = tuple(map(lambda x: bool(int(x)), elements_input.split()))

if all_true(user_tuple):
        print("All elements of the tuple are true.")
else:
        print("Not all elements of the tuple are true.")
