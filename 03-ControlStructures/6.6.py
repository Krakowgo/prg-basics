parking_hours = int(input('Parking hours: '))
price = 0

if parking_hours >= 1 and parking_hours <= 2:
    price = 5
elif parking_hours >= 3 and parking_hours <= 6:
    price = 15
else:
    price = 20

print(f'Your parking fee is {price} PLN.')