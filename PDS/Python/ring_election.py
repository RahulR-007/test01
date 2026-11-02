# Simplified ring election: circulate active IDs and choose maximum.
processes = [10, 20, 30, 40, 50]
failed = 50
active = [p for p in processes if p != failed]
print("Election message circulating:")
for p in active:
    print("Process", p, "participates")
print("New coordinator:", max(active))
