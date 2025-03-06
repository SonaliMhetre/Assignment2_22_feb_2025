#Use a lambda function with filter( ) to get all even numbers from a list: [1, 2, 3, 4, 5, 6, 7, 8].


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  
