def f(amount_to_pay):
    payment = amount_to_pay
    count = 0

    while payment > 0:
        if payment >= 5:
            payment -= 5
            count += 1
        elif payment >= 2:
            payment -= 2
            count += 1 
        elif payment >= 1:
            payment -= 1
            count += 1
    return count
print(f(23))