def isPalindrome(s):
    reverse = s[::-1]
    return (s == reverse)

print(isPalindrome("racecar"))
print(isPalindrome("hello"))