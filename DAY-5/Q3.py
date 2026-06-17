str = input("Enter String =")
substr = input("Enter SubString =")
if(substr in str):
    print("Substring found!!")
elif(substr not in str):
    print("Substring NOT found!!")