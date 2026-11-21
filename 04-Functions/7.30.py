def sum_natural(n):
    outcome = 0
    first_digit = 1

    for i in range(first_digit,n + 1):
        outcome += i
    return outcome
print(sum_natural(10))