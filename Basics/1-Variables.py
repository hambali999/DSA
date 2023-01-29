# INTEGER
age = 21
old = 40

print(age)
print(old)

print("You are "  + str(age) + " years old")
print("You are", age, "years old")
print(f"You are {age} years old")
print("You are {} years old, going old in {}".format(age, old))

# FLOAT
price = 20.01
print(f"The price is ${price}")

# STRING
name = "Bro"
print(f"My name is {name}")

# BOOLEAN
online = True
for_sale = False
running = False
print(f"Are you online?:  {online}")
print("Is the item for sale?: {}".format(for_sale))
print(f"Game running: {running}")
print("RUNNING" if running else "NOT RUNNING")

# if running:
#     print("The game is running")
# else:
#     print("Nope not running")

