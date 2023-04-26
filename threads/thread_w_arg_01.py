import threading

def my_function(value):
    print("Value received:", value)

# Create a new thread and pass a value to the function
my_thread = threading.Thread(target=my_function, args=("Hello, world!",))

# Start the thread
my_thread.start()

# Wait for the thread to finish before exiting the program
my_thread.join()
