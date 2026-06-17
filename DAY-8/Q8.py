#Takes 6 numbers as input from the user and stores them in a set (duplicates
# should be removed automatically).
a = int(input("Enter a Number = "))
b = int(input("Enter a Number = "))
c = int(input("Enter a Number = "))
d = int(input("Enter a Number = "))
e = int(input("Enter a Number = "))
f = int(input("Enter a Number = "))

numbers = {a, b, c, d, e, f}

print("numbers = ",numbers)
print(type(numbers))

# Adds two more numbers using add().
numbers.add(90)
numbers.add(80)
print("Updated Set = ",numbers)

# Removes one number safely using discard().
numbers.discard(90)
print("After Discard 90 = ",numbers)

# Prints the final set and its length using len().
print("final Set = ",numbers)
print(numbers.__len__)