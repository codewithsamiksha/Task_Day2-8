str = input("Enter a String = ")
print("One by One Character =")
for i in range(len(str)):
    print(i,":",str[i])

print("String in Reverse")
for i in range(len(str) -1, -1, -1):
    print(str[i], end = "")
