# Learning is valld vs is not valid

def isValid(n):
    valid = False
    if(n == 1):
        valid = True
    elif(n == 2):
        valid = True
    elif(n == 3):
        valid = True
    elif(n == 4):
        valid = True
    elif(n == 5):
        valid = True
    else:
        valid = False
    return valid

a = False
b = True
c = False
d = False
e = True
f = True

x = ((a or b) and (f and not(c))) or ((d or c) or (e or not(f)))

n = input("Please enter a number 1-5: ")

print(x)