import math

circumference = int(input('Enter tree circumference in cm: '))
diameter = circumference / math.pi

able_to_cut = diameter >= 50

print(f'Tree can be cut down: {able_to_cut}')