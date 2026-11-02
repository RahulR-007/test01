# Hypercube maximum-ID reduction for 4 processes (2 dimensions).
ids = [10, 25, 15, 30]
n = len(ids)
step = 1
print("Initial IDs:", ids)
while step < n:
    old = ids.copy()
    for i in range(n):
        partner = i ^ step
        ids[i] = max(old[i], old[partner])
    print("After round:", ids)
    step *= 2
print("Leader ID:", ids[0])
