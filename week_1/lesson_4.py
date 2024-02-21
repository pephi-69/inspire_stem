def print_diamond(rows):
    for i in range(1, rows + 1):
        print(" " *(rows - i) + "*" * (2 * i - 1))
    for i in range(rows - 1, 0, -1):
        print(" " * (rows -i) + "*" * (2 * i - 1) )
         
rows = 9     
print_diamond(rows)    

def print_triangle(rows):
    for i in range(1, rows + 1):
        print("*" * i)

rows = 25
print_triangle(rows)         

def print_box(width, height):
    horizontal_border = " + " + " - " * (width - 2)+ '+'
    inner_space = ' | ' + ' ' * ( width + 2) +'|'

    print(horizontal_border)
    for _ in range( height - 2):
        print(inner_space)
        print(horizontal_border)

print_box(10 , 5)
     