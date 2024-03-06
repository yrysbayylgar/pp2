from functools import reduce

def multiply(x, y):
    return x * y

def multiply_numbers(numbers):
    if not numbers:
        return 0
    result = reduce(multiply, numbers)
    return result

# Example usage
elements = input()
elements_list = [int(e) for e in elements.split()]
result = multiply_numbers(elements_list)

if result == 0:
    print("0")
else:
    print(result)
