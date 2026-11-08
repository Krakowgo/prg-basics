user_temperature = int(input('Input temperature'))

if user_temperature > 35:
    print('It is extremely hot')
elif user_temperature > 30:
    print('It is hot')
elif user_temperature >= 15:
    print('It is warm')
elif user_temperature >= 0:
    print('It is cold')
else:
    print('Warning for frost')