list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Using extend() to add list2 to list1.
list2.extend(list1)
print("List2 = ",list2)
#print the list2 that is exdend with list1

#Using append() to add list2 to a copy of list1.
list2.append(list1)
print("list 2 =",list2)
#print list2 that is extended and list 1 that is appended