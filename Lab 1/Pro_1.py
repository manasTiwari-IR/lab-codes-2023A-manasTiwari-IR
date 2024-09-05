# lab program 1
def Sum(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return(a*b)
def division(a,b):
    if b == 0 :
        return "Cannot divide by zero"

    return a/b
def integerQuo(a,b):
    if b == 0:
        return "Cannot divide by zero"

    return a//b
def remainder(a,b):
    if b == 0:
        return "Cannot divide by zero"

    return a%b

x = int(input("Enter one number : "))
y = int(input("Enter second number : "))
print(Sum(x,y))
print(substract(x,y))
print(multiply(x,y))
print(division(x,y))
print(integerQuo(x,y))
print(remainder(x,y))
