user_time = int(input('Enter time (24 hours format): '))
time_in_12 = 0

if 13 <= user_time < 24:
    time_in_12 = user_time - 12
    print(f'Time in 12-hour format: {time_in_12}pm')
elif 1 <= user_time <= 11:
    print(f'Time in 12-hour format: {user_time}am')
else:
    print(f'Time in 12-hour format: {user_time}pm')