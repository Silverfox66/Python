def my_function(x, y):
    if(x > y):
        return x - y
    else:
        return x + y

x = 5
y = 3

z = my_function(x, y)

x = 2
y = x + z

print(z)
print(y)
print(z)
#Play with debug