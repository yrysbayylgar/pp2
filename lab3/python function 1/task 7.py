def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

examp = input()
alist = [int(num) for num in examp.split()]

result = has_33(alist)
print(result)

