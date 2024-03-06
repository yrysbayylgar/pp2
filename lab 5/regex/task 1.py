import re

pattern = re.compile(r'a+b*')
mystr = input()

match = pattern.fullmatch(mystr)

if match:
    print('matches')
else:
    print('does not match')
