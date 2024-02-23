#This is a program to show pascals triangle
#Date :22/2/2024
#Name:Ephraim

z = 15
for i in range(z):
 print(' '*(z -1), end=" ")
 print(' '.join(map(str,str(11**i))))