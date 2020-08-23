#Deleting dictionary elements

#creating a dictionary
cubes = {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
print(cubes)

#remove a particular item
print(cubes.pop(3))

#remove an arbitary items
print(cubes.popitem())

print(cubes[2])

#Delete the dictionary itself
del cubes[4]
print(cubes)

