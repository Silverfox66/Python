def print_names_by_letter(names, letter):
    for name in names:
        if(name[0] == letter):
            print(name)
names = ["Alice", "Bob", "Andrew", "Walter", "Kevin", "Audrey"]
print_names_by_letter(names, 'A')