P = True  # 2 + 2 = 4
Q = False # 1 + 3 = 5 (incorrect)
R = True  # 3 + 3 = 6

results = {
    "P and Q": P and Q,
    "P or Q": P or Q,
    "Not(P)": not P,
    "Not(Q)": not Q,
    "Not(P) or Q": not P or Q,
    "Not(P or Q)": not (P or Q),
    "Not(P and Q)": not (P and Q),
    "(P and Q) or R": (P and Q) or R,
    "P and (Q or R)": P and (Q or R),
    "P and (Not(Q and R))": P and not (Q and R)
}

print(results)