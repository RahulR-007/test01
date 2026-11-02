# Simplified Bully election: highest active process ID wins.
processes = [1, 2, 3, 4, 5]
failed = 5
print("Processes:", processes)
print("Process", failed, "failed")
active = [p for p in processes if p != failed]
print("Election started")
for p in active:
    if p < failed:
        print("Process", p, "joins election")
    elif p > failed:
        print("Process", p, "responds")
print("New coordinator:", max(active))
