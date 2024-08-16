#item assignment is not allowed in tuples

tup=(2,1,3,1)
print(type(tup))
print(tup)
print(tup[0])
print(tup[1])
print(len(tup))
print(tup[0:2]) #slicing

#empty tuple
tup1=()
print(type(tup1))
print(tup1)
 
#single value tuple
tup2=(1,)
print(type(tup2))
print(tup2) 

#index in tuple(print the first index of the element )
tup3=(1,2,3,1,4)
print(tup3.index(1))

#count 
tup4=(1,2,3,4,1,4,5)
print(tup4.count(1))

"""tup.reverse() #reverse is not allowed in tuples
print(tup) #reverse is not allowed in tuples
tup.append(4) #append is not allowed in tuples
print(tup) #append is not allowed in tuples
tup.sort() #sorting is not allowed in tuples
print(tup) #sorting is not allowed in tuples
#tup[0]=5
#print(tup)"""