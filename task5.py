import threading
import queue
import sys

# Create a shared queue to hold items
shared_queue = queue.Queue()

# Function for the producer
def producer(thread_id, num_productions):
    for i in range(num_productions):
        item = f"Item {i} from Producer {thread_id}"
        shared_queue.put(item)
        print("**********************",shared_queue.get())
        print(f"Produced {item}")

# Function for the consumer
def consumer(thread_id):
    while True:
        item = shared_queue.get()
        if item is None:
            break
        print(f"Consumed {item}")
        shared_queue.task_done()

def main():
    if len(sys.argv) != 3:

        sys.exit(1)

    num_producers = int(sys.argv[1])
    num_consumers = int(sys.argv[2])

    # Create producer threads
    producer_threads = []
    for i in range(num_producers):
        thread = threading.Thread(target=producer, args=(i, 5))
        producer_threads.append(thread)

    # Create consumer threads
    consumer_threads = []
    for i in range(num_consumers):
        thread = threading.Thread(target=consumer, args=(i,))
        consumer_threads.append(thread)

    # Start producer and consumer threads
    for thread in producer_threads:
        thread.start()

    for thread in consumer_threads:
        thread.start()

    # Wait for all producer threads to finish
    for thread in producer_threads:
        thread.join()

    # Add None to the queue for each consumer to signal them to exit
    for i in range(num_consumers):
        shared_queue.put(None)

    # Wait for all consumer threads to finish
    for thread in consumer_threads:
        thread.join()

    print("All producers and consumers have finished!")

if __name__ == "__main__":
    main()
