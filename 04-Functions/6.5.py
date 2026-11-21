import range

x = 2
y = 15
number = 7
result = ''

in_range = range.f(x,y)

print(f'A number: 7')
if in_range:
    result = 'Yes'
else:
    result = 'No'
print(f'Number {number} in the range <{x},{y}>: {result}')