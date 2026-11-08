previous_price = 200.00
current_price = 140.00
discount = 100 - (current_price / previous_price) * 100

if discount >= 10:
    print('Buy the product!') 
    print(f'Product price reduced by {discount}%')