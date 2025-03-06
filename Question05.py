#Write a recursive function factorial(n) to calculate the factorial of a number.

def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: factorial of n is n * factorial(n-1)
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output will be 120