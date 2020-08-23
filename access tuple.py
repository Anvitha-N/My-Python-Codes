#Accessing elements from tuples:

tuple1 = ('knowledge','morals','skills','ethics')
tuple2 = (10,20,30)
tuple3 = ('car','bus','jeep')
tuple = ('engineer')

print(tuple1)

#concatenation
print(tuple2 + tuple3)

#nested tuples
tuple4 = (tuple1 , tuple3)
print(tuple4)

#repetition
tuple = ('engineer',)*5
print(tuple)

#slicing in tuples
print(tuple1[1:])
print(tuple2[::-1])
print(tuple3[1:3])

#length of tuple
print(len(tuple1))
print(len(tuple3))

print (tuple1[1])
print (tuple2[2],tuple1[2])



