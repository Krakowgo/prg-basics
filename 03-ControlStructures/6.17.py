user_time = (input('Enter time (24 hours format): '))
hours = int(user_time[0:2])
minute = user_time[3:5]
hours_in_12 = 0

if 13 <= hours < 24:
    hours_in_12 = hours - 12
    print(f'Time in 12-hour format: {hours_in_12}:{minute}pm')
elif 1 <= hours <= 11:
    print(f'Time in 12-hour format: {hours}:{minute}am')
elif hours == 24:
    hours_in_12 = hours - 24
    print(f'Time in 12-hour format: {hours_in_12}:{minute}am')
elif hours == 12:
    hours_in_12 = hours
    print(f'Time in 12-hour format: {hours_in_12}:{minute}pm')
else:
    print(f'Time in 12-hour format: {hours}:{minute}pm')