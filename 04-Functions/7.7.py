def f(binary_number):
    is_binary = True
    string_number = str(binary_number)
    binary_count = 0
    count = 0

    while count < len(string_number):
        for i in string_number:
            if i == '1' or i == '0':
                binary_count += 1 
            else:
                is_binary = False
            count += 1
    if binary_count == len(string_number):
        is_binary = True
    else:
        is_binary = False
    return is_binary

print(f(1332))