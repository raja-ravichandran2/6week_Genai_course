# ==========================================
# PYTHON COLLECTION TYPES DEMO
# List, Tuple, Set, Dictionary
# ==========================================

print("===== PYTHON COLLECTION TYPES =====\n")


# ==========================================
# 1. LIST
# ==========================================

print("1. LIST")

# List creation
fruits = ["Apple", "Banana", "Mango"]

print("Original List:", fruits)

# Add item
fruits.append("Orange")
print("After append:", fruits)

# Remove item
fruits.remove("Banana")
print("After remove:", fruits)

# Access item
print("First item:", fruits[0])

print("-----------------------------------\n")


# ==========================================
# 2. TUPLE
# ==========================================

print("2. TUPLE")

# Tuple creation
colors = ("Red", "Green", "Blue")

print("Tuple:", colors)

# Access item
print("First color:", colors[0])

# Length
print("Tuple length:", len(colors))

print("-----------------------------------\n")


# ==========================================
# 3. SET
# ==========================================

print("3. SET")

# Set creation
numbers = {1, 2, 3, 4}

print("Original Set:", numbers)

# Add item
numbers.add(5)
print("After add:", numbers)

# Remove item
numbers.remove(2)
print("After remove:", numbers)

print("-----------------------------------\n")


# ==========================================
# 4. DICTIONARY
# ==========================================

print("4. DICTIONARY")

# Dictionary creation
student = {
    "name": "John",
    "age": 21,
    "course": "Python"
}

print("Dictionary:", student)

# Access value
print("Student Name:", student["name"])

# Add new key-value pair
student["city"] = "Chennai"

print("Updated Dictionary:", student)

print("-----------------------------------\n")


# ==========================================
# END
# ==========================================

print("Program completed successfully!")