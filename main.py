import threading

# Global variable to store the input string
input_string = ""

# Flag to indicate whether the input thread is done
input_done = False

# Lock to synchronize access to the input string
input_lock = threading.Lock()

# Flag to indicate whether the reverse thread is done
reverse_done = False

# Lock to synchronize access to the reverse_done flag
reverse_lock = threading.Lock()

# Flag to indicate whether the capital thread is done
capital_done = False

# Lock to synchronize access to the capital_done flag
capital_lock = threading.Lock()

# Flag to indicate whether the shift thread is done
shift_done = False

# Lock to synchronize access to the shift_done flag
shift_lock = threading.Lock()

def input_thread_func():
    global input_string, input_done
    try:
        # Get the input from the user
        input_string = input("Enter a string: ")
    except Exception as e:
        # Handle any exceptions that may occur while getting the input
        print("Exception in input thread:", e)
    finally:
        # Set the input_done flag to indicate that the input thread is done
        with input_lock:
            input_done = True

def reverse_thread_func():
    global input_string, reverse_done
    # Wait until the input thread is done
    while not input_done:
        pass
    try:
        # Reverse the input string
        reversed_string = input_string[::-1]
        print("Reversed string:", reversed_string)
    except Exception as e:
        # Handle any exceptions that may occur while reversing the string
        print("Exception in reverse thread:", e)
    finally:
        # Set the reverse_done flag to indicate that the reverse thread is done
        with reverse_lock:
            reverse_done = True

def capital_thread_func():
    global input_string, capital_done
    # Wait until the input thread is done
    while not input_done:
        pass
    try:
        # Capitalize the input string
        capitalized_string = input_string.upper()
        print("Capitalized string:", capitalized_string)
    except Exception as e:
        # Handle any exceptions that may occur while capitalizing the string
        print("Exception in capital thread:", e)
    finally:
        # Set the capital_done flag to indicate that the capital thread is done
        with capital_lock:
            capital_done = True

def shift_thread_func():
    global input_string, shift_done
    # Wait until the input thread is done
    while not input_done:
        pass
    try:
        # Shift each character in the input string by two
        shifted_string = ""
        for c in input_string:
            shifted_string += chr(ord(c) + 2)
        print("Shifted string:", shifted_string)
    except Exception as e:
        # Handle any exceptions that may occur while shifting the string
        print("Exception in shift thread:", e)




# Create the input thread
input_thread = threading.Thread(target=input_thread_func)

# Create the reverse thread
reverse_thread = threading.Thread(target=reverse_thread_func)

# Create the capital thread
capital_thread = threading.Thread(target=capital_thread_func)

# Create the shift thread
shift_thread = threading.Thread(target=shift_thread_func)

# Start the input thread
input_thread.start()

# Start the reverse thread
reverse_thread.start()

# Start the capital thread
capital_thread.start()

# Start the shift thread
shift_thread.start()

# Wait for the input thread to finish
input_thread.join()

# Wait for the reverse thread to finish
reverse_thread.join()

# Wait for the capital thread to finish
capital_thread.join()

# Wait for the shift thread to finish
shift_thread.join()

