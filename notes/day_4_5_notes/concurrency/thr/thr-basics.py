'''
Tries to run in windows - threads does not run concurrently
             in onlinegdb - threads run concurrently 


'''

import time 
import threading

def print_numbers():
    id = threading.get_ident()
    for i in range(5):
        print(f'{i}@{id}')
        time.sleep(0.025)

threads = []
for I in range(5):
    thread = threading.Thread(target=print_numbers)
    threads.append(thread)
    thread.start()  # Start the thread
for I in range(5):    
    threads[I].join()   # Wait for the thread to finish

print_numbers()