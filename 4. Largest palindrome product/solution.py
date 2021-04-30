def isPalindrome(number):
    if str(number)[::-1]==str(number):
        return True
    return False

x1 = 999
x2 = 999
palindromes = []
while x1>0 and x2>0:
    y = x1*x2
    if isPalindrome(y):
        palindromes.append(y)
    if x1==x2:
        x1 = 999
        x2 -= 1
    else:
        x1 -= 1

print(max(palindromes))