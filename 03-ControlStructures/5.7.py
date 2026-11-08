import time
i = 10

while i >= 1:

    if i == 5:
        print('Five')
    elif i == 4:
        print('Four')
    elif i == 3:
        print('Three')
    elif i == 2:
        print('Two')
    elif i == 1:
        print('One')
    else:
        print(f'{i}')
    
    time.sleep(1)
    i -= 1

print('Zero')

    

