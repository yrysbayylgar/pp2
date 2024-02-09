def convert(grams):
    ounces = 28.3495231 * grams
    return ounces

grams = float(input())
ounces = convert(grams)

print(ounces)

