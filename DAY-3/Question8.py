def factorial(n):
    if( n == 1):
        print(n)
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Enter a Number:- "))
result = factorial(num)
print("factorial of ", num , "is" , result)