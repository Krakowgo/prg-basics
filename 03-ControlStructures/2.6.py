user_number = int(input('Input number here: '))
number = ''

if user_number > 0:
    number = 'positive'
    print(f'Number {user_number} is {number}')
elif user_number < 0:
    number = 'negative'
    print(f'Number {user_number} is {number}')
else:
    print('Number is 0')