x = 10
y = 5
print(f"Addition: {x + y}")
print(f"Subtraction: {x - y}")
print(f"Multiplication: {x * y}")
print(f"Division: {x / y}")
print(f"Floor Division: {x // y}") # Rounds down to the nearest whole number
print(f"Modulo (Remainder): {x % y}")



num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")



# Print numbers from 1 to 5
for i in range(1, 6):
    print(i)

# Iterate through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
