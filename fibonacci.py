#Learning fibonacci sequence

def fib(n, table = dict()):
    if(n <= 1):
        return 1
    if(n in table):
        return table[n]
    else:
        table[n] = fib(n - 1) + fib(n - 2)
        return table[n]

print("fib:", fib(50))