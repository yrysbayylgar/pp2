import re

def match_pattern(input_string):
    pattern = re.compile(r'ab{2,3}')
    match = pattern.fullmatch(input_string)

    if match:
        print('matches the pattern.')
    else:
        print('does not match the pattern.')

input_string = input()
match_pattern(input_string)
