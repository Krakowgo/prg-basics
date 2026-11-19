def f(number):
    string_number = str(number)
    sum = 0

    for i in string_number:
        if string_number.count(i) >= 2:
            sum += int(i)
    return sum
print(f(1027))