###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# define temperature in degrees Celsius
celsius = int(input('Input temperature in Celsius: '))

# Converting from Celsius to Kelvin and Fahrenheit
fahrenheit = celsius * 1.8 + 32
kelvin = celsius + 273.15

# results
print(f'In Fahrenheit: {fahrenheit}, In kelvin: {kelvin}')