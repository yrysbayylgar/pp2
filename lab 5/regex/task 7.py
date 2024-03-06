snake_case = input()

words = snake_case.split('_')

camel_case = words[0] + ''.join(word.capitalize() for word in words[1:])

print(f"Camel case: {camel_case}")
