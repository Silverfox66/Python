# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# number = int(input("Type number you would like to factorialize: "))
# result = factorial(number)
# print(f"The factorial of {number} is: {result}")

# def factorial(n):
#     if(n == 0):
#         return 1
#     result = 1
#     for x in range(1, n + 1):
#         result *= x
#     return result

# n = 6
# result = factorial(n)
# print("result", result)

# def areaOfTriangle(base, height):
#     area = 0.5* base * height
#     return area

# base = int(input("Type number you would like your base to be: "))
# height = int(input("Type number you would like your height to be: "))
# area = areaOfTriangle(base, height)
# print("area:", area)

# m = factorial(int(areaOfTriangle(base, height)))
# print("m:", m)

n=0
for x in range(65, 70):
    n+=1
print(n)
