from Circle import Circle
from Triangle import triangle
from rhombus import rhombus
from square import square
while True:
    print("type 'circle' to print circle")
    print("type 'square' to print square")
    print("type 'rhombus' to print rhombus")
    print("type 'triangle' to print triangle")
    print("type 'exit' to exit")
    S=input('Enter your specific shape:')
    print('press 1 for area')
    print('press 2 for perimeter')
    print('press 3 for circumference')
    A=int(input('Enter your choice:'))
    if S== 'circle' and A==1:
        radius=float(input('Enter your radius:'))
        circle1=Circle(radius)
        print('Area:',circle1.area)
    elif S == 'circle' and A == 2:
        radius = float(input('Enter your radius:'))
        circle2 = Circle(radius)
        print(circle2.perimeter)
    else:
        print('Please enter your choice:')
    if S== 'square' and A == 1:
        side = float(input('Enter your side:'))
        square1 = square(side)
        print(square1.area)
    elif S== 'square' and A == 2:
        side = float(input('Enter your side:'))
        square2 = square(side)
        print(square2.perimeter)
    if S== 'rhombus' and A == 1:
        side = float(input('Enter your side:'))
        rhombus1 = rhombus(side)
        print(rhombus1.area)
    elif S== 'rhombus' and A == 2:
        side = float(input('Enter your side:'))
        rhombus2 = rhombus(side)
        print(rhombus2.perimeter)
    if S== 'triangle' and A == 1:
        side = float(input('Enter your side:'))
        triangle1 = triangle(side)
        print(triangle1.area)
    elif S== 'triangle' and A == 2:
        side = float(input('Enter your side:'))
        triangle2 = triangle(side)
        print(triangle2.perimeter)

