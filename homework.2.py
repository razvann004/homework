def sum_numbers(*args):
    total_sum = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            total_sum += arg
        elif isinstance(arg, list):
            for num in arg:
                if isinstance(num, (int, float)):
                    total_sum += num
    return total_sum
print(sum_numbers(1, 5, -3, 'abc', [12, 56, 'cad']))  # Output: 3
print(sum_numbers())  # Output: 0
print(sum_numbers(2, 4, 'abc'))  # Output: 6




def sum_all_nums(n):
    if n == 0:
        return 0, 0, 0  # base case: return 0 for all sums
    else:
        all_sum, even_sum, odd_sum = sum_all_nums(n-1)
        all_sum += n
        if n % 2 == 0:
            even_sum += n
        else:
            odd_sum += n
        return all_sum, even_sum, odd_sum
all_sum, even_sum, odd_sum = sum_all_nums(10)
print("Sum of all numbers from 0 to 10:", all_sum)  # output: 55
print("Sum of even numbers from 0 to 10:", even_sum)  # output: 30
print("Sum of odd numbers from 0 to 10:", odd_sum)  # output: 25

def read_integer():
    try:
        value = int(input("Enter an integer: "))
        return value
    except ValueError:
        return 0
num = read_integer()
print("The entered value is:", num)





