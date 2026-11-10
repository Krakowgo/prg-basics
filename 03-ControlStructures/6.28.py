first_digit = '0'
second_digit = '1'
big_string = ''
big_string = big_string + ' ' + first_digit + ' ' + second_digit + ' '

for i in range(0,19):
    next_digit = int(first_digit) + int(second_digit)
    big_string = big_string + str(next_digit) + ' '
    first_digit = second_digit
    second_digit = next_digit
print(big_string)
