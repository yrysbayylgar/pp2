import re

pattern = re.compile(r'[A-Z][a-z]+')
mystr = input()

matches = pattern.findall(mystr)

if matches:
    print('Sequence')
else:
    print('No sequences')
