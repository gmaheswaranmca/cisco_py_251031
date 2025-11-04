'''
Problem Statement
    We want to simulate a Task Processing System where:
    Producer processes generate numbers and put them into a shared queue.
    Consumer processes fetch numbers, square them, and store results in a shared dictionary.
    Synchronization (Lock, Semaphore, Condition) ensures safe updates to shared resources.
    Inter-process communication (IPC) uses Queue, Pipe, Value, Array, Dict, List.
    A Process Pool can also be used to handle some tasks in parallel.
'''

import multiprocessing
import time
import random

# Producer function
def producer(start, end, q, cond):
    for i in range(start, end + 1):
        with cond:  # Acquire condition lock
            q.put(i)
            print(f"Producer {multiprocessing.current_process().name} produced {i}")
            cond.notify()  # Notify consumers
        time.sleep(0.2)

# Consumer function
def consumer(q, results, lock, cond, sem, arr, val):
    while True:
        with cond:
            while q.empty():
                cond.wait(timeout=2)
                if q.empty():
                    return  # Stop if no tasks

            num = q.get()

        with sem:  # Limit number of consumers
            result = num * num

            with lock:  # Lock for writing results
                results[num] = result
                arr[num - 1] = result  # Store in shared array
                val.value += 1         # Increment shared counter
                print(f"Consumer {multiprocessing.current_process().name} processed {num} => {result}")

# Function for Process Pool
def pool_task(x):
    return x * x

# Example using Pipe
def pipe_worker(conn):
    conn.send("Hello from child process!")
    conn.close()

def main():
    # Manager for shared objects
    manager = multiprocessing.Manager()
    results = manager.dict()
    q = manager.Queue()
    cond = manager.Condition()
    lock = manager.Lock()
    sem = manager.Semaphore(2)  # Max 2 consumers at a time
    arr = multiprocessing.Array('i', 10)  # Shared array of 10 ints
    val = multiprocessing.Value('i', 0)   # Shared integer value

    # Create producer processes
    p1 = multiprocessing.Process(target=producer, args=(1, 5, q, cond), name="P1")
    p2 = multiprocessing.Process(target=producer, args=(6, 10, q, cond), name="P2")

    # Create consumer processes
    c1 = multiprocessing.Process(target=consumer, args=(q, results, lock, cond, sem, arr, val), name="C1")
    c2 = multiprocessing.Process(target=consumer, args=(q, results, lock, cond, sem, arr, val), name="C2")

    p1.start(); p2.start()
    c1.start(); c2.start()

    p1.join(); p2.join()
    c1.join(); c2.join()

    print("\nFinal Results Dictionary:", dict(results))
    print("Shared Array:", list(arr))
    print("Total tasks processed (Value):", val.value)

    # Process Pool Example
    with multiprocessing.Pool(processes=3) as pool:
        numbers = [1, 2, 3, 4, 5]
        squared = pool.map(pool_task, numbers)
        print("\nProcess Pool Results:", squared)

    # Pipe Example
    parent_conn, child_conn = multiprocessing.Pipe()
    pipe_proc = multiprocessing.Process(target=pipe_worker, args=(child_conn,))
    pipe_proc.start()
    print("Message from pipe:", parent_conn.recv())
    pipe_proc.join()

if __name__ == "__main__":
    main()

'''
Explanation
    Creating a Process & Callbacks
        multiprocessing.Process(target=producer, args=(...)) creates producer/consumer processes.
        pool.map(pool_task, numbers) demonstrates process pool callback.
    Passing Arguments & Return Values
        Producers take (start, end) ranges.
        Consumers process tasks and update shared objects.
        Process pool directly returns squared results.
    Process Synchronization
        Lock → ensures only one process updates results at a time.
        Condition → consumers wait for producers to add tasks.
        Semaphore → limits number of active consumers.
    Inter-Process Communication (IPC)
        Queue → for producer-consumer task sharing.
        Dict, Array, Value → for storing results across processes.
        Pipe → for direct two-way communication.
    Process Pools
        multiprocessing.Pool handles multiple tasks in parallel without manually creating processes.
'''