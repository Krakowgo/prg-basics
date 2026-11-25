
def f(n):
    count = 0
    number = 2

    while count < n:
        prime = True

        for i in range(2, number):
            if number % i == 0:
                prime = False
                break

        if prime == True:
            count += 1

        if count == n:
            return number

        number += 1


print(f(1))
print(f(5))