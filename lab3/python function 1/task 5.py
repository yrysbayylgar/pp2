def generate_permutations(string, result=''):
    if not string:
        print(result)
    else:
        for i in range(len(string)):
            remain = string[:i] + string[i+1:]
            generate_permutations(remain, result + string[i])

word = input()
generate_permutations(word)