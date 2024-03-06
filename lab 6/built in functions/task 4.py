import time
import math

def calculate_square_root(number, delay_ms):
    time.sleep(delay_ms / 1000) 
    result = math.sqrt(number)
    return result

number_in = input()
delay_in = input()
number = float(number_in)
delay_ms = int(delay_in)
result = calculate_square_root(number, delay_ms)

print(f"Square root of {number} after {delay_ms} milliseconds is {result:.15f}")
