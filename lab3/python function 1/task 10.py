def unique_list(alist):
    unique=[]
    for x in alist:
        if x not in unique:
            unique.append(x)
    return unique

examp = input()
thelist = [int(num) for num in examp.split()]

result = unique_list(thelist)
print(result)
