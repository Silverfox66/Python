F1= 1
F2 = 2

Fn = F1 + F2
sum = 2
while(Fn <= 4000000):
    if(Fn % 2 == 0):
        sum += Fn
    F1 = F2
    F2 = Fn
    Fn = F1 + F2

print("sum:", sum)