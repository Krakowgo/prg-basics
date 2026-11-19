def f(password):
    user_pass = password
    is_valid = True
    if len(user_pass) < 6:
        is_valid = False
    else:
        for i in user_pass:
            if user_pass.count(i) >= 2:
                break
    return is_valid
print(f("A2water3"))