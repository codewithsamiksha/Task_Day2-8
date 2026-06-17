scores = [85, 92, 78, 92, 65, 92, 88]
print("Original List = ",scores)

#find and print the index of the first occurrence of 92.
print("Index of first occurrence of 92 = ", scores.index(92)) 

#Count and print how many times 92 appears.
print("Number 92 of = ",scores.count(92))

#take a number as input and check is exist or not
num = int(input("Enter a Number to check in a List = "))
print("Index of a Number = ",scores.index(num))
print("Count of a Number = ",scores.count(num))