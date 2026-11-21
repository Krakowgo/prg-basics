def f(detector):
    is_full = False
    count =0
    for i in detector:
        if i == "+":
            count += 1
            if count > 2:
                is_full = True
        else:
            count -= 1
    return is_full
print(f("+-++-++-+---"))