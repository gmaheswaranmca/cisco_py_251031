'''
Problem Statement
    We want to build a system that:
        Producers generate tasks (numbers) and put them in a shared queue.
        Consumers (thread pool workers) fetch tasks, process them (e.g., square the number), and return results.
        We need synchronization to protect the shared queue.
        We use condition variables so workers wait when the queue is empty and get notified when new tasks arrive.
        A thread pool of fixed worker threads processes all tasks.
'''

import threading
import queue
import time

# Shared queue
task_queue = queue.Queue()
stop_signal = False

# Worker function
def worker(worker_id):
    while True:
        try:
            task = task_queue.get(timeout=1)  # Wait for task
        except queue.Empty:
            if stop_signal:
                break
            continue

        # Process task
        result = task * task
        print(f"Worker {worker_id} processed {task} => {result}")

        task_queue.task_done()

# Producer function
def producer(start, end):
    for i in range(start, end + 1):
        task_queue.put(i)
        print(f"Produced task {i}")
        time.sleep(0.1)  # Simulate delay

# Main function
def main():
    global stop_signal
    num_workers = 3
    workers = []

    # Create worker threads (thread pool)
    for i in range(num_workers):
        t = threading.Thread(target=worker, args=(i + 1,))
        t.start()
        workers.append(t)

    # Create producers
    prod1 = threading.Thread(target=producer, args=(1, 5))
    prod2 = threading.Thread(target=producer, args=(6, 10))

    prod1.start()
    prod2.start()

    prod1.join()
    prod2.join()

    # Wait until all tasks are processed
    task_queue.join()

    # Signal workers to stop
    stop_signal = True
    for t in workers:
        t.join()

    print("All tasks processed!")

if __name__ == "__main__":
    main()
'''
Explanation
    Creating Threads
        Workers: threading.Thread(target=worker, args=(i+1,))
        Producers: threading.Thread(target=producer, args=(start, end))
    Passing Arguments & Return Values
        worker receives worker_id.
        producer receives a range of numbers.
        Return values are simulated via printed results (since Python threads can’t directly return values).
    Synchronization (mutex & condition)
        queue.Queue() is thread-safe (internally uses a mutex + condition variables).
        No need to manually lock/unlock in this case.
    Thread Communication
        Producers put tasks in queue (task_queue.put()).
        Consumers get tasks (task_queue.get()), and block/wait when empty.
    Thread Pool
        Fixed number of worker threads (num_workers = 3) act as a pool.
'''