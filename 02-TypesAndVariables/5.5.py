price_amount = input("Enter the price: ")
price = float(price_amount)

discount_amount = input("Enter the discount % : ")
discount = float(discount_amount)

discount_rate = (100 - discount) / 100
price_with_discount = price * discount_rate
reduction = price - price_with_discount

print(f'Product price is {price:.2f}')
print(f'Discount amount is {discount:.0f}%')
print(f'Price with the discount is {price_with_discount:.2f}')
print(f'Reduction amount is {reduction:.2f}')
