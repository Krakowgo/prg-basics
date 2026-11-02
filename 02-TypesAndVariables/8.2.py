###
# Calculation of circle area and circumference 
#

# determine radius and PI values

radius = int(input("Input radius here: "))
pi = 3.14
# calculate area 
area = radius * radius * pi
# calculate circumference 
circumference = 2 * radius * pi
# print results
print(f'circumference = {circumference}, area = {area}')