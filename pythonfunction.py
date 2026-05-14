# =====================================================
# ADVANCED PYTHON DEMO PROGRAM
# Covers:
# 1. Operators
# 2. If / Nested If
# 3. Loops
# 4. Functions
# 5. Error Handling
# 6. File Handling
# =====================================================

print("===== PYTHON ADVANCED CONCEPTS =====\n")


# =====================================================
# 1. OPERATORS
# =====================================================

print("1. OPERATORS")

a = 10
b = 5

# Arithmetic Operators
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Comparison Operators
print("a > b :", a > b)
print("a == b :", a == b)

# Logical Operators
print("a > 5 and b < 10 :", a > 5 and b < 10)

print("-----------------------------------\n")


# =====================================================
# 2. IF / NESTED IF
# =====================================================

print("2. IF / NESTED IF")

age = 20

if age >= 18:
    print("Person is an Adult")

    # Nested If
    if age >= 60:
        print("Senior Citizen")
    else:
        print("Young Adult")

else:
    print("Person is Minor")

print("-----------------------------------\n")


# =====================================================
# 3. LOOPS
# =====================================================

print("3. LOOPS")

# For Loop
print("FOR LOOP")
for i in range(1, 6):
    print("Number:", i)

print()

# While Loop
print("WHILE LOOP")
count = 1

while count <= 5:
    print("Count:", count)
    count += 1

print("-----------------------------------\n")


# =====================================================
# 4. FUNCTIONS
# =====================================================

print("4. FUNCTIONS")

# Function Definition
def add_numbers(x, y):
    return x + y

# Function Call
result = add_numbers(15, 25)

print("Addition Result:", result)

print("-----------------------------------\n")


# =====================================================
# 5. ERROR HANDLING
# =====================================================

print("5. ERROR HANDLING")

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

    result = 100 / number
    print("100 divided by number =", result)

except ValueError:
    print("Error: Please enter only numbers.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

finally:
    print("Error handling section completed.")

print("-----------------------------------\n")


# =====================================================
# 6. FILE HANDLING
# =====================================================

print("6. FILE HANDLING")

# Writing to a file
file = open("sample.txt", "w")

file.write("Welcome to Python File Handling.\n")
file.write("This file was created using Python.")

file.close()

print("Data written to sample.txt")

# Reading from a file
file = open("sample.txt", "r")

content = file.read()

print("\nReading File Content:")
print(content)

file.close()

print("-----------------------------------\n")


# =====================================================
# PROGRAM END
# =====================================================

print("Program completed successfully!")