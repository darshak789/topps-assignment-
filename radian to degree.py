#Write a Python program to convert degree to radian.
star = '\u2605'
separator = '\u25ac'
bullet_point = '\u25cf'
arrow = '\u2794'
white_florette= '\u2740'
ending=white_florette+'-'*30+'End'+'-'*30+white_florette

print(f'{star} Write a Python program to convert degree to radian.')
print(f'{separator} ' * 35)

import math
degree=180.00
print(f'{arrow} {degree} is equal to {math.radians(degree)} radians.')
#radians = degrees * (pi / 180)
#half circle represents pi radian and complete circle 2pi radians which is 360 degree.
#90 degree=pi/2 radian