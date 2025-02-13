#Checking a number for small things

def problem1(n):
    if n >= 0:
        return True
    else:
        return False
def problem2(n):
    if n < 1 or n > 5:
        return True
    else:
        return False
def problem3(n):
    if n > 15:
        return True
    else:
        return False
def problem4(n):
    if (1 <= n <= 5) or (12 <= n <= 20):
        return True
    else:
        return False