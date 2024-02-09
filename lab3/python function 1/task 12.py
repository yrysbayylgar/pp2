def histogram(numbers):
    for a in numbers:
        print('*' * a)

examp = input()
numbs = [int(x) for x in examp.split()]

histogram(numbs)