student = ('Rahul', 20, 'Computer Science', 'A')

#Iterate through the tuple using a for loop and print each item.
for range in student:
    print(range)


#Unpack the tuple into four variables (name, age, branch, grade) 
print("Unpack the tuple into four variables =")
name , age , branch , grade = student
print("Name = ",name)
print("Age= ", age)
print("Branch = ",branch)
print("Grade= ",grade) 