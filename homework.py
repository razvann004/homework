my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

sorted_list = sorted(my_list)
print(sorted_list)

my_list_descending = sorted(my_list, reverse=True)
print(my_list_descending)

even_numbers = [num for num in my_list if num % 2 == 0]
print(even_numbers)

odd_numbers = [num for num in my_list if num % 2 != 0]
print(odd_numbers)

multiple_of_three = [num for num in my_list if num % 3 == 0]
print(multiple_of_three)
