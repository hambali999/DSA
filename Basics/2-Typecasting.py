# typecasing = The process of converting a value of one data type to another
# (string, integer, float, boolean)
# Explicit vs Implicit

name = "Bro"
age = 21
gpa = 1.9
student = True


print(type(name))
print(type(age))
print(type(gpa))
print(type(student))
print("===")

# explicit conversion - manually converting a value of one data type to another

age = float(age)
print(age)
print(type(age))
print("===")

print(round(gpa))
gpa = int(gpa)
print(gpa)
print(type(gpa))
print("===")

# implicit type casting - automatically 

x = 2
y = 2.0

x = x/y
print(x)

