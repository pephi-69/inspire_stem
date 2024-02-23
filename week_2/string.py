#strings in python
#Date :22/2.2024
#Name:Ephraim

city = "nairobi"
#getting a single character in a string
print(city[0])#N
print(city[1])#a
print(city[2])#i
print(city[3])#r
print(city[4])#o
print(city[5])#b
print(city[6])#i
print(city[-1])
print(city[-2])
#convert to upper case
print(city)
print("\n")# prints a new line
print(city.upper())
name ="EPHRAIM"
print(name)
print(name.lower())#converts to lowercase

town = " Naivasha"

print(town)
print("\t")#prints new tab
print(town.strip())
#.strip removes any whitespace before or trailing string
print('\t')

#added strings
f_name ='Vin' 
s_name ='Diesel'
full_name= f_name +s_name
print(full_name)

#replacing characters
fruit ='Mango'
print(fruit.replace('o',"a"))

subject = 'physical:sciences'
print(subject.split(":"),)

age =18
height = 1.2
print("I am {0} years old and {1} meters tall".format(age,height))
      