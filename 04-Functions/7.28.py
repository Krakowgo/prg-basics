def f(dice):
    out_come = ''
    max_counter = 0
    for i in dice:
        c = dice.count(i)
        if c > max_counter:
            max_counter = c
            out_come = i
    return out_come
print(f("2133"))