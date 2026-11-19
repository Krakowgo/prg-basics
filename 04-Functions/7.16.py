def f(n):
    times = n - 2
    a = 0
    b = 1
    i = 0
    while i < times:
        temp = a + b
        a = b
        b = temp
        i += 1
    return temp
print(f(5))