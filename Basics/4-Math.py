import math

# Basic arithmethic operators

friends = 5
friends += 1
friends -= 2
friends *= 3
friends /= 2
friends **= 2
remainder = friends % 5
print(friends)
print(remainder)
print("===")

# Built in math related functions

x = 3.14
y = -4
z = 5
result1 = round(x)
result2 = abs(y) #abs = absolute
result3 = pow(2, 3)
result4 = max(x,y,z)
result5 = min(x,y,z)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print("===")

print(math.pi) #pi = pi
print(math.e) #e = exponential constant
x = 9
y = 3.1
print(math.sqrt(x))
print(math.ceil(y))
print(math.floor(y))
print("===")

# Exercises - Circumference of a cirlc
# C = 2 * pi * r
radius = float(input("Enter the radius of a circle: "))
circumference = 2*math.pi*radius
print(f"The circumference of the cirlcle is {round(circumference, 2)}")