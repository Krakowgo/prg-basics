user_number = int(input('Enter number: '))

def sum_digits(user_number):
    absolute_number = abs(user_number)
    string_number = str(absolute_number)
    total = 0
    for i in string_number:
        i = int(i)
        total += i
    return total
print(f'The sum of the digit in the numbger {user_number} is {sum_digits(user_number)}')