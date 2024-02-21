#This is a program to calculate surface area
#Date :20/2/2024
#Name :Ephraim

#surface area  of cylinder

import math

r = int(input("Enter the radius : "))
pi = float(math.pi)
d = int((r * 2))
h = int(input("Enter the height"))

c = ((pi * r **2) + (pi * d * h))

print("The surface area of cylinder",c)

#surface area of a sphere
r = int(input("Enter the radius : "))
pi = float(math.pi)

s =((4 * pi * r **4))
print("The surface area of sphere",s)

#Surface area of a cone
r = int(input("Enter the radius : "))
pi = float(math.pi)
l = int(input("Enter the length"))

s =((pi * r** 2) + (pi * r * l))
print("The surface area of cone",s)
