import re

mystr = input()

result = re.sub(r'([a-z])([A-Z])', r'\1 \2', mystr)

print(result)
