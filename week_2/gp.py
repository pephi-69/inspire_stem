#This is a program to calculate the geometric progression 
#Date : 20/2/2024
#Name :Ephraim

a = int(input("Enter the constant  "))
r = int(input("Enter the factor : "))
n = int(input ("Enter the term : "))

b = (a * r ** (n-1))

print("The solution of the gp",b)