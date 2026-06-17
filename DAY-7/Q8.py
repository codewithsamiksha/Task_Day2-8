fruits = ('apple', 'banana', 'cherry', 'banana', 'mango', 'apple')

#Find and print the first index of 'banana'.
print("First Index Of Banana = ",fruits.index('banana'))

#Find and print the first index of 'banana' starting the search from index 2.
print("Index Of Banana = ",fruits.index('banana',2))

#Use try-except to safely find the index of 'kiwi' and print "Not found" if it
# doesn't exist.
try:
    print("Index of kiwi:", fruits.index('kiwi'))
except ValueError:
    print("Not found")
