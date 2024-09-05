#lab program 2
# find area , perimeter and all the angles of a triangle
import math

def perimeter(a,b,c):
    print("Perimetr is : ",a+b+c)
def area(a,b,c):
    s = (a+b+c)/2;
    A = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area is : ",A)
def angles(a,b,c):
    A = math.degrees(math.acos((b**2 + c**2 - a**2)/(2*b*c)))
    B = math.degrees(math.acos((a**2 + c**2 - b**2)/(2*a*c)))
    C = 180 - A - B;
    print("angles are : ",A,B,C)
    
x = int(input("first side : "))
y = int(input("first side : "))
z = int(input("first side : "))
perimeter(x,y,z)
area(x,y,z)
angles(x,y,z)
