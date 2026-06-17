set1 = {1, 2, 3}
set2 = {3, 4, 5, 6}
print("original set =",set1)
#Make a copy of set1.
set1_copy = set.copy(set1)
print("copy of set1 = ",set1_copy)

#Update set1 with elements from set2 using update().
set1.update(set2)
print("Updated set = ",set1)