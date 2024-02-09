def volume(radius):
    volume = (4 / 3) * 3.14159 * radius**3
    return volume

radius = float(input())
result = volume(radius)
print(result)