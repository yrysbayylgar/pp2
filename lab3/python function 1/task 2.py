def convert(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

fahrenheit = float(input())
celsius = convert(fahrenheit)
print(celsius)
