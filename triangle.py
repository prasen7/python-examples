# program to calculate check if triangle can be made, given the sides.
# and to calculate the field of triangle using Heron's formula.
def isItATriangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
    
def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5
    
def fieldOfTriangle(a, b, c):
    if not isItATriangle(a, b, c):
        return None
    return heron(a, b, c)

a = float(input("Enter the first side's length: "))
b = float(input("Enter the second side's length: "))
c = float(input("Enter the third side's length: "))

if isItATriangle(a, b, c):
    print("Congratulations - it can be a triangle.")
    print(fieldOfTriangle(a,b,c))
else:
    print("Sorry, it won't be a triangle.")
    
print(fieldOfTriangle(1., 1., 2. ** .5))
    
