import re

mystr = input()

snake_case = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', mystr).lower()

print(snake_case)
