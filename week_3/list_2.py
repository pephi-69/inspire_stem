#This is a continuation of list
#Date : 28 / 02/2024
#Name : Ephraim

friends = ['Simon','Hellen','Jose','Tess','Manu']
for friend in friends :
    print(friend)

enemies = friends[:]#copy one list into another


for enemy in enemies :
    print(enemy)    

fruits = ['mango','banana','guava','oranges']
print(fruits[0:3])#slicing a list
print("\t")
print("\t")



del fruits[0]
print(fruits)    

squares = [] #initializes a list

for x in range (0,11) :
    squares.append(x**2)
print(squares)