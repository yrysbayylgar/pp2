def is_palindrome(s):
    alllow = ''.join(s.lower().split())
    if(alllow == alllow[::-1]):
        return True
    else:
        return False

examp = input()
result = is_palindrome(examp)

if result:
    print("It's a palindrome")
else:
    print("It's not a palindrome")

