#Create a loop that prints all numbers from 1 to 20 but skips multiples of 5.

for num in range(1, 21):
    if num % 5 == 0:
        continue
    print(num)
