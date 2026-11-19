def f(number1, number2, number3):
    numbers = number1, number2, number3
    sum = 0
    max_number = max(numbers)
    min_number = min(numbers)
    sum = max_number - min_number
    return sum
print(f(12,2,8))

    