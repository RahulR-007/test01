import threading

def task(number):
    print("Hello from thread", number)

threads = []
for i in range(3):
    t = threading.Thread(target=task, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Main thread completed")
