#Define a function sum_numbers(a, b=10) that takes two numbers and returns their sum. If the second number is not provided, it should default to 10.

def sum_numbers(a, b=10):
    return a + b
print(sum_numbers(5))      # Output: 15 (5 + 10)
print(sum_numbers(5, 7))   # Output: 12 (5 + 7)
