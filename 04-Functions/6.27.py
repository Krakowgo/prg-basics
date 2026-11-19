def f(product_code):
    sum_numbers = 0
    user_reminder = int(product_code[3])
    is_afourth = True

    for i in product_code[:3]:
        sum_numbers += int(i)

    system_reminder = sum_numbers % 7

    if user_reminder == system_reminder:
        is_afourth = True
    elif user_reminder != system_reminder:
        is_afourth =False
    return is_afourth
print(f("2035"))