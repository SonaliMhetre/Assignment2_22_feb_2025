#Write a function is_even(n) that returns True if a number is even, otherwise False.

def is_even(n):
    return n % 2 == 0
result = is_even(8)
print(result)  # This will print True

result = is_even(7)
print(result)  # This will print False