def f(x,y):
    out_put = 0
    first_digit = x
    second_digit = y

    for i in range(first_digit, second_digit):
        if i < 0 and i % 2 == 0:
            out_put += 1
    return out_put
print(f(-1,11))