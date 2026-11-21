def f(product_code):
    is_code = True
    add_digit = product_code[0:3]
    last_digit = product_code[3]
    sum = 0

    for i in add_digit:
        sum += int(i)
    remainder = sum % 7
    if remainder == int(last_digit):
        is_code = True
    else:
        is_code = False
    return is_code
print(f("2035"))