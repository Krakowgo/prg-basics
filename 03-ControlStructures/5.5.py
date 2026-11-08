###
# Sums numbers entered by user
#
total_sum = 0
mean = 0
user_numbers = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    user_numbers += 1

    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    mean = total_sum / user_numbers

print(f"The total sum of the numbers is: {total_sum}")
print(f"The mean of the numbers is: {mean}")