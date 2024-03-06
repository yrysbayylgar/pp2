def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

user_input = input()
if is_palindrome(user_input):
    print("a palindrome")
else:
    print("not a palindrome")
