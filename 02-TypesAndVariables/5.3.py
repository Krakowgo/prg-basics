###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('a=')
side_a = int(a)

b = input('b=')
side_b = int(b)

c = input('c=')
side_c = int(c)

cube_volume = side_a * side_b * side_c
cube_surface_area = 2 * (side_a * side_b + side_b * side_c + side_a * side_c)
print(f'The volume of a cuboid with side {side_a} and {side_b} and {side_c} is {cube_volume}')
print(f'The surface area of a cuboid with side {side_a} and {side_b} and {side_c} is {cube_surface_area}')