coordinates = (10 , 20)
coordinates =[(coordinates)]
print("Convert Tuple into List")
print(type(coordinates))

coordinates[0] = 15
coordinates.append(25)
print("Changed list = ",coordinates)

print("Convert List Into Tuple")
coordinates = tuple(coordinates)
print(type(coordinates))
print("Changed Tuple = ", coordinates)