def f(n):
    output = ""
    first_ast = "*"
    asterisks = "*" * (n - 1)
    display = ""
    if n > 1:
        for i in asterisks:
            combo = "/" + i
            output += combo
        display = first_ast + output
    elif n == 1:
        display = first_ast
    else:
        display = ""
    return display
print(f(2))
