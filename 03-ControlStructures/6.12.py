product_price = int(input('Product price: '))
product_number = int(input('Number of products purchassed: '))
char = 0
payment = 0
sum = 0

for char in range(1,product_number + 1):
    if char <= 2:
        payment = product_price 
    else:
        payment = product_price - (product_price * 0.25)

    sum += payment

print(f'Amount to pay: {sum}')