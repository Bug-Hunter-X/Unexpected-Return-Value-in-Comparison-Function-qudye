def my_function(a, b):
    if a > b:
        return a
    else:
        return b

result = my_function(5, 2)
print(result)  # Output: 5

result = my_function(2, 5)
print(result)  # Output: 5

result = my_function(-3, 0)
print(result)  # Output: 0

result = my_function(-5,-3)
print(result) # Output: -3