# Thread
# https://docs.python.org/3/library/threading.html
import threading
import time

def thread_main(x):
    print(f'{x} - Thread Start')
    time.sleep(1)
    print(f'{x} - Thread End')
 
print('----- Threads Start -----')
thread_main(0) 
thread_main(1)
thread_main(2)
thread_main(3)
thread_main(4)
thread_main(5)
thread_main(6)
thread_main(7)
thread_main(8)
thread_main(9)
print('----- Threads End -----') 

print('----- Multi Threads Start -----') 
threads = []
for i in range(10):
    t = threading.Thread(target=thread_main, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
print('----- Multi Threads End -----') 

# Thread Lock - Critical Section
number = 0
lock = threading.Lock()

def thread_counter(x):
    global number
    print(f'{x} - Thread Start - {number}')
    lock.acquire()
    time.sleep(1)
    number += 1
    print(f'{x} - Thread End - {number}')
    lock.release()
 
print('----- Threads Start -----')
thread_counter(0) 
thread_counter(1)
thread_counter(2)
thread_counter(3)
thread_counter(4)
thread_counter(5)
thread_counter(6)
thread_counter(7)
thread_counter(8)
thread_counter(9)
print('----- Threads End -----') 

print('----- Multi Threads Start -----') 
number = 0
threads = []
for i in range(10):
    t = threading.Thread(target=thread_counter, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
print('----- Multi Threads End -----')