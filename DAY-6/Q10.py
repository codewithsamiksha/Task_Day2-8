#Take 5 subject marks as input from the user and store them in a list.
m1 = int(input("Enter marks 1 = "))
m2 = int(input("Enter marks 2 = "))
m3 = int(input("Enter marks 3 = "))
m4 = int(input("Enter marks 4 = "))
m5 = int(input("Enter marks 5 = "))
marks = [m1,m2,m3,m4,m5]

#Print the list.
print("marks = ",marks)


#Add one more subject mark using append().
marks.append(52)
print("m6 appended = ",marks)

#Print the highest and lowest marks (using built-in functions).
# marks.higest()
# print(marks)

#Sort the marks in descending order.
marks.sort()
marks.reverse()
print("descending Order = ",marks)

#Calculate and print the average marks.
result= m1 + m2 + m3 + m4 + m5 + 52
average = result/6

print("Average Marks = ",average)

#Use len() to show total number of subjects.
marks.__len__
print("length of list = ",marks)