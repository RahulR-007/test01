import threading
import time

semaphore = threading.Semaphore(2)

def task(number):
    with semaphore:
        print("Thread", number, "entered")
        time.sleep(1)
        print("Thread", number, "leaving")

threads = []
for i in range(5):
    t = threading.Thread(target=task, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
print("All threads completed")
