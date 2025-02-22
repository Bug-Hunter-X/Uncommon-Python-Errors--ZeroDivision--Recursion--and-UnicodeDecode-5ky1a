def function_with_uncommon_error(data):
    try:
        # Simulate an error in processing data
        result = 1 / data if data != 0 else 0 # Handle ZeroDivisionError
        return result
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: Division by Zero")
        return 0  # Return a default value
    except Exception as e:
        print(f"Caught an unexpected exception: {e}")
        return None  # Handle other unexpected issues

data = 10
result = function_with_uncommon_error(data) 
print(f"Result: {result}") #Handle the returned None value appropriately

#Handle RecursionError with a check for base case
def recursive_function(n, max_depth=1000):
    if n < 0:
        return 0
    elif n > max_depth:
        raise RecursionError("Maximum recursion depth exceeded")
    else:
        return recursive_function(n - 1, max_depth) + n

#Example of Handling UnicodeDecodeError
import os
try:
    if not os.path.exists('nonexistent_file.txt'):
        print('File not found')
    else:
        with open('nonexistent_file.txt', 'r', encoding='utf-8', errors='ignore') as f:
             content = f.read()
        print(content)
except FileNotFoundError:
    print("File not found. Creating dummy file")
    with open('nonexistent_file.txt','w') as f:
        f.write('Test')
except UnicodeDecodeError as e:
    print(f"UnicodeDecodeError caught: {e}")
    print("Trying again with different encoding")
    with open('nonexistent_file.txt', 'r', encoding='latin-1', errors='ignore') as f:
        content = f.read()
    print(content)