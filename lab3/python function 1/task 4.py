def is_prime(numbers):
    def check_prime(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
 
    return [num for num in numbers if check_prime(num)]
 
input_numbers = input()
numbers_list = [int(num) for num in input_numbers.split()]
result = is_prime(numbers_list)
 
print(result)
