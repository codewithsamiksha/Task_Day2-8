str = input("Enter String = ")
print("Length of String = ",len(str))
mid = len(str)//2
print("First Half = ",str[:mid])
print("Second Half = ",str[mid:])

if ("python" in str.lower()):
    print("python is present in string")
else:
    print("python is not present")

for i in range(len(str)):
    print("Positive Index= ",i,"Negative Index = ", i -len(str), "Cg" \
    "haracter",str[i])

print("Reverse String = ",str[: : -1])