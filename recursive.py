def S(n, memo={1: 5, 2: 6, 3: 7}):
    if n in memo:
        return memo[n]
    memo[n] = S(n-1, memo) * S(n-2, memo) * S(n-3, memo)
    return memo[n]

print(S(1))  
print(S(2))  
print(S(3))  
print(S(4)) 
print(S(5))  
print(S(6))  
print(S(7))