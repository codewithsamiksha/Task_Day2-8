#Takes a set of 5 colors as input from the user.
c1 = input("Enter Color name = ")
c2 = input("Enter Color name = ")
c3 = input("Enter Color name = ")
c4 = input("Enter Color name = ")
c5 = input("Enter Color name = ")

colors = {c1, c2, c3, c4, c5}
print("Set = ",colors)
print(type(colors))

#Asks the user to enter a color name.
check_col = input("Enter a Color name to Check = ")

#Checks whether the color is present in the set using in and not in.
if(check_col in colors):
    print(check_col,"is Present")
elif(check_col not in colors):
    print(check_col,"is not Present")