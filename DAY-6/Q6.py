items = [10, 20, 30, 20, 40, 50]
print("Original List = ",items)

items.remove(20)            #remove 20 using remove().
print("removed 20 = ",items)

items.pop(-2)               #remove 3 using pop()
print("remove index 3 using pop() = ",items)

items.pop(-1)               #Remove last elementusing pop
print("Remove last element = ",items)

items.clear()               #clear entire list
print("list = ", items)