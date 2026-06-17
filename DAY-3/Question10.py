# num = 1
# while True:
#    num = int(input("Enter a Number:-"))
#    if(num<=0):
#        break

def get_number():
    num = int(input("Enter a Number:-"))
    return num

number = get_number()
print("Your Entered Number" , number)

def is_even():
    num = int(input("Enter a Number:-"))
    if(num % 2 == 0):
        print("Number is True" , num)
    else:
        print("Number is false" , num)

    print("Square of a Number is :-" ,num**2)

is_even()



