
from range_module import check_range

number = int(input("A number: "))

result = check_range(number, 2, 15)

if result == True:
    print("Number", number, "in the range <2,15>: yes")
else:
    print("Number", number, "in the range <2,15>: no")