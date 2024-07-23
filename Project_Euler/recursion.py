# def sum(n):
#     sum = 0
#     for x in range(1, n + 1):
#         sum += x
#     return sum

# print("sum:", sum(5))



def sumR(n):
    if(n == 1):
        return n
    return n + sumR(n - 1)

print("sum:", sumR(5))