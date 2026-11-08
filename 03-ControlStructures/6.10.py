dog_age = int(input("Your dog's age: "))
dog = 0
age_rate = 0
sum_age = 0
sum1 = 0
sum2 = 0

for dog in range(1,dog_age +1):
    if dog <= 2:
        age_rate = 10.5
    else:
        age_rate = 4

    sum_age += age_rate
print(f'The age of dog in dog year is: {sum_age}: ')
