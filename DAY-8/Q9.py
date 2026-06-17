scores = [85, 92, 78, 92, 85, 88, 95, 78]
# Convert the list to a set.
scores_set = {85, 92, 78, 92, 85, 88, 95, 78}
print("list converted into set = ",scores_set)
print(type(scores_set))

# Print the unique scores.
print("Unique Scores = ",scores_set)

# Convert the set back to a sorted list and print it.
scores = [85, 92, 78, 92, 85, 88, 95, 78]
print("Sorted list = ",scores.sort())
print(type(scores))



# Print the total number of unique scores.
print("Total of Unique score = ",scores.count())