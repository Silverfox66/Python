#Compare two sets


# def letterCount(string, char):
#     count = 0
#     for x in string:
#         if(x == char):
#             count += 1

# def hasLetter(string, char):
#     for x in string:
#         if(x == char):
#             return True
#     return False
# string = "hello"
# char = 'l'
# count = letterCount(string, char)
# print("count:", count)

def compare_sets(set1, set2):
    if set1 == set2:
        print("Sets are equal")
    elif set1 > set2:
        print("A is greater than B")
    elif set1 < set2:
        print("A is less than B")
    elif set1 >= set2:
        print("A is greater than or equal to B")
    elif set1 <= set2:
        print("A is less than or equal to B")


A = {1, 2, 3}
B = {1, 2}

compare_sets(A, B)
