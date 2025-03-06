#Write a loop that stops when it encounters the number 7 in this list: [1, 2, 3, 4, 5, 6, 7, 8, 9].

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in numbers:
    if num == 7:
        break
    print(num)
