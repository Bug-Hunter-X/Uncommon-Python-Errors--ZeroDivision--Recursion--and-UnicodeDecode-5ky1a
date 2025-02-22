def function_with_uncommon_error(data):
    try:
        # Simulate an error in processing data
        result = 1 / 0  # ZeroDivisionError
        return result
    except ZeroDivisionError:
        print("Caught ZeroDivisionError")
        return None
    except Exception as e:
        print(f"Caught an unexpected exception: {e}")
        return None

data = 10
result = function_with_uncommon_error(data) 
print(f"Result: {result}") #Handle the returned None value appropriately

# Example of another uncommon error: RecursionError
def recursive_function(n):
    if n < 0:
        return 0
    else:
        return recursive_function(n - 1) + n #Uncomment to cause RecursionError
recursive_function(10000) # Increase value to cause RecursionError

#Example of UnicodeDecodeError
with open('nonexistent_file.txt', 'r', encoding='utf-8') as f:
     content = f.read()
print(content)