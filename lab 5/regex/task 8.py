import re

mystr = input()
result= re.findall('[A-Z][^A-Z]*', mystr)

print(result)
