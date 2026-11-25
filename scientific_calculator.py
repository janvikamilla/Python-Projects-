import math

print("===== SCIENTIFIC CALCULATOR =====")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square Root")
print("6. Power")
print("7. Sine")
print("8. Cosine")

choice = int(input("Enter your choice: "))

if choice in [1, 2, 3, 4, 6]:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", a + b)

    elif choice == 2:
        print("Result:", a - b)

    elif choice == 3:
        print("Result:", a * b)

    elif choice == 4:
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero!")

    elif choice == 6:
        print("Result:", a ** b)

elif choice == 5:
    number = float(input("Enter number: "))
    if number >= 0:
        print("Square Root:", math.sqrt(number))
    else:
        print("Invalid number!")

elif choice == 7:
    angle = float(input("Enter angle in degrees: "))
    print("Sine:", math.sin(math.radians(angle)))

elif choice == 8:
    angle = float(input("Enter angle in degrees: "))
    print("Cosine:", math.cos(math.radians(angle)))

else:
    print("Invalid choice!")
