def isPalindrome(x):
    num = x
    if num < 0:
        num *= -1
    reverse = ""
    while num != 0:
        reverse += str((num % 10))
        num //= 10
    if x == int(reverse):
        return True
    else:
        return False

print(isPalindrome(121))
