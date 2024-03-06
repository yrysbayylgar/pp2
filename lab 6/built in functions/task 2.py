def count_upper_lower(string):
    upper_count = sum(1 for char in string if char.isalpha() and char.isupper())
    lower_count = sum(1 for char in string if char.isalpha() and char.islower())
    return upper_count, lower_count

user_input = input()
upper, lower = count_upper_lower(user_input)
print(f"uppercase letters: {upper}")
print(f"lowercase letters: {lower}")
