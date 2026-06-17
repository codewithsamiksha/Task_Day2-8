import math
import random
square = lambda x:math.sqrt(x)
print("Square =",square(9))

def calculate_power(base,exp):
    return math.poe(base, exp)

def generate_randome():
    return random.randint(1,100)

while True:
    print("/n 1. Square")
    print("2. Power")
    print("3.Random Number")
    print("4. Exit")
    choice = int(input("Enter your Choice ="))

    if(choice==4):
        print("Exit")
        break


    elif(choice==1):
        num = float(input("Enter a Number ="))
        print("Square=",square(num))

    if(choice==2):
        base = float(input("Enter base ="))
        exp = float(input("Enter exponent ="))
        print("power=",math.pow(base,exp))

    elif(choice==3):
        print("Random Number =",generate_randome())


