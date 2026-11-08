users_age = int(input('Your age: '))
group = ''
if users_age <13:
    group = 'Child'
elif 13 <= users_age <= 19:
    group = 'Teen'
elif 20 <= users_age <= 64:
    group = 'Adult'
else:
    group = 'Senior'

print(f'Your age group is {group}')