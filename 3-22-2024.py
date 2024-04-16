# f = open("Data/input.txt", 'r')
# animals = []
# for x in f:
#     animals.append(x.strip())
# f.close()
# animals.sort
# f = open("Data/output.txt", 'w')
         
# for x in animals:
#     f.write(x)
#     f.write('\n')


# f.close()
zoo1 = {"tigers", "bears", "lions", "cheetahs", "turtles"}
zoo2 = {"cheetahs", "turtles", "giraffes", "lions", "pandas"}
zoo3 = {"pandas", "lions", "giraffes", "fish", "wolves"}
union = zoo1.union(zoo2)
print("union", union)

intersection = zoo2.intersection(zoo3) 
print("intersection:", intersection)

difference = zoo1.difference(zoo2)
print("differnce:", difference)

print((zoo1.union(zoo2)).difference(zoo3))