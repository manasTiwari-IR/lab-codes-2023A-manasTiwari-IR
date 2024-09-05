#Lab program 3
# Convert Celcius to Fahrenheit
def convert(C):
    F = (C * 1.8) + 32;
    print("In Fahrenheit = ",F)
    
c = float(input("Enter temperature in Celcius : "))
convert(c)