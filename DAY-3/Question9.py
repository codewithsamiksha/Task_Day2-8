total = 5          #global keyword
def add_value(x):   #local keyword
    print("value of global keyword" , total)

    print("value of local keyword" , x)

    print("total:-" , total + x )

add_value(5)



