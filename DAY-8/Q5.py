s = {100, 200, 300, 400, 500}
print("Original Set = ",s)
#Use pop() to remove and print one element.
print(s.pop())

#Print the set after popping.
print("After Poped = ",s)

#Clear the entire set using clear().
print("Remove Entire Set = ",s.clear())

#Print the final empty set.
print("set= ",s)

#by using remove() remove the element in list if the element is not present in the list it will show error
#as same in discard but is we discard the element that is not present it will not display any error
# and by using pop() we can remove the element that is located at the last memory location 