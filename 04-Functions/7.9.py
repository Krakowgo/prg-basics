def f(number,even):
    str_number = str(number)
    sum = 0
    even_number = 0
    odd_number = 0

    for i in str_number:
        if int(i) % 2 == 0:
            even_number += int(i)
        else:
            odd_number += int(i)
    if even == True:
        sum = even_number
    else:
        sum = odd_number
    return sum
print(f(3124,False))