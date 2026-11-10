user_number = int(input('Enter prime number: '))
big_string = '2'
first_number = 3
found = 0

while found < user_number:
    for i in range(2,first_number):
        if first_number % i == 0:
            break
        else:
            big_string = big_string + ' ' + str(first_number)
            print(len(big_string))
    first_number += 1
    found += 1
print(f'Prime numbers: {big_string}')