#Take input for name, roll number, 3 subject marks.
name = input("Enter Your Name = ")
roll_no = int(input("Enter your RollNo = "))
m1 = int(input("Enter Marks of Subject 1 = "))
m2 = int(input("Enter Marks of Subject 2 = "))
m3 = int(input("Enter Marks of Subject 3 = "))

#Store all information in a tuple (use packing).
tup = (name , roll_no , m1 , m2 , m3)

#Print the complete record.
print("Created Tuple = ",tup)

#Unpack the tuple and print each value with proper labels.
print("Unpack the tuple")
name , roll_no , m1 , m2 , m3 = tup
print("Name = ",name)
print("Rollno = ",roll_no)
print("marks1 = ",m1)
print("Marks2",m2)
print("Marks3= ",m3)

#Use count() to check how many times a particular mark appears (if any).
marks = int(input("Enter marks"))
print("Count of Marks = ",tup.count(marks))

#Create a nested tuple to store multiple student records (at least 2 students)
# andaccess specific values.
nested_records = (("Renuka","11",85) , ("Prem","12",89))

print("Student 1 name = ",nested_records[0][0])
print("Student 1 RollNo = ",nested_records[0][1])
print("Marks Student 1 = ",nested_records[0][2])

print("Student 2 name = ",nested_records[1][0])
print("Student 2 RollNo = ",nested_records[1][1])
print("Marks Student 1 = ",nested_records[1][2])