def hide(card_number):
    numbers = str(card_number)
    result = ''
    first_digit = numbers[0:2]
    second_digit = "*" * 10
    third_digit = numbers[-4:]

    result = first_digit + second_digit + third_digit
    return result 
