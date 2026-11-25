def power(x, n):

    # Base case
    if n == 0:
        return 1

    # Recursive case
    if n > 0:
        return x * power(x, n - 1)


# Calculate 5^3
print(power(5, 3))