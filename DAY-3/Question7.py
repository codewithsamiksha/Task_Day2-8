def coundown(n):
    if(n==1):
        return 1
    print(n)
    coundown(n-1)

coundown(10)