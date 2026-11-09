user_number = int(input('Enter number: '))
operator = 1
sum_of_number = 0

while operator < 11:
    sum_of_number = user_number * operator
    print(f'{user_number} x {operator} = {sum_of_number}')  
    operator += 1