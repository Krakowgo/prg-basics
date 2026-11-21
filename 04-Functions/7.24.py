def f(expression):
    sum = int(expression[0])
    number = 0
    operater = ""
    for i in range(1,len(expression),2):
        operater = i
        number = int(expression[i + 1])
        if operater == "+":
            sum += number
        elif operater == "-":
            sum -= number
    return sum
print(f("2+3"))
    