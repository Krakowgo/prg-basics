N = int(input('Enter your number: '))
prime_number = ''
i = 0
counter = 0 
deviser = 2

while counter < N:
        is_prime = True
        for i in range(2,deviser):
               if deviser % i == 0:
                      is_prime = False
                      break
        if is_prime:
               print(deviser, end=" ")
               counter += 1
        deviser += 1