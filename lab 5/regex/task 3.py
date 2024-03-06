import re

pattern = re.compile(r'[a-z]+_[a-z]+')
mystr = input()

matches = pattern.findall(mystr)

if matches:
    print('Sequence')
else:
    print('No sequences')

