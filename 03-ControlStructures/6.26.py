correct_pin = '0805'
attenpt = 0

while attenpt < 3:
    user_pin = input('Enter your code: ')
    if len(user_pin) == 4 and user_pin.isdigit():
        if user_pin == correct_pin:
            print('Your PIN is correct!!')
        else:
            print('Incorrect...')
            attenpt += 1
print('Sorry, your payment card has been blocked.')