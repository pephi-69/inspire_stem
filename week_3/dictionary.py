#I have no laptop

my_phone = {"make ":"oppo","color":"gray","year":"2023","weight":"0.2kg"}

print(my_phone["weight"])
print(my_phone["year"])    

#to change the values in a dictionary
my_phone["color"] = 'red'
my_phone["year"] ='2008'
my_phone["size"] = "120mm x 60mm"
del my_phone["color"]#to delete an entry 


for key,value in my_phone.items() :
    print(key)
    print(value)
    print("\n")

my_phone_2 = my_phone.copy
print(my_phone_2)

#using dictionary describe your favourite car<print individual values and key ,copy to another
#My favourite car

Favourite_car = {"make":"English","year":"2008","Engine":"V6","color":"red"} 
print(Favourite_car["make"])
print(Favourite_car["Engine"])
print(Favourite_car["year"])
print(Favourite_car["color"])

for key,value in Favourite_car.items() :
    print(key)
    print(value)
    print("\n")

car = Favourite_car.copy() :
print(key)
print(value)
print("\n")