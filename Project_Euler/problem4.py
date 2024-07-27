def isPalindrome(s):
    reverse = s[::-1]
    return (s == reverse)

max = 0
for x in range(100, 1000):
    for y in range(100, 1000):
        product = x * y
        if(isPalindrome(str(product))):
            if(product > max):
                max = product