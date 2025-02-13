#Defines a function that takes a list of names and a letter as input, then prints the names from the list that start with the given letter.
def print_names_by_letter(names, letter):
    for name in names:
        if(name[0] == letter):
            print(name)
names = ["Alice", "Bob", "Andrew", "Walter", "Kevin", "Audrey"]
print_names_by_letter(names, 'A')