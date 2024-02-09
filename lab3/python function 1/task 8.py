def spy_game(nums):
    sequence = [0, 0, 7]
    for num in nums:
        if num == sequence[0]:
            sequence.pop(0)
            if not sequence:
                return True
    return False

examp = input()
alist = [int(num) for num in examp.split()]

result = spy_game(alist)
print(result)