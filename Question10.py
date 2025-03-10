#Write a program that checks if a year is a leap year. (Hint: A year is a leap year if it is divisible by 4 but not by 100, except when it is also divisible by 400.)

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Example usage
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
