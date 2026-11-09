user_number = int(input('Enter decimal number: '))
start_num = user_number
bin_number = ''

while user_number > 1:
    user_number = user_number / 2
    if user_number % 2 == 0:
        bin_number = bin_number + '0'
    else:
        bin_number = bin_number + '1'

if user_number == 1:
    bin_number = bin_number + '1'

bin_number[::-1]
print(f'{start_num}(10) = {bin_number}(2)')