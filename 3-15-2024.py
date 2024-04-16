A = {"deer", 5, "oven"}
B = {"panda", 15, "k"}

# if(A.issubset(B)):
#     print("Yes")
# else:
#     print("No")

# if(A <= B):
#         print("Yes")
# else:
#     print("No")

# if(A.issuperset(B)):
#     print("Yes")
# else:
#     print("No")

# if(A >= B):
#         print("Yes")
# else:
#     print("No")

intersection = A.intersection(B)
union = A.union(B)
print("intersection:", intersection)
print("union", union)

difference = A.difference(B)
print("difference", difference)
difference = B.difference(A)
print("differnce:", difference)



