#set methods
collection1={3,4,5,6,7,8,"sunjid","monira"}
#add method
collection1.add("hello") #add method to add an element in the set
collection1.add("world") #add method to add an element in the set
collection1.add(1) #add method to add an element in the set
collection1.add(2) #add method to add an element in the set
print(collection1)
#remove method
collection1.remove("hello") #remove method to remove an element from the set
print(collection1)
collection1.remove(1) #remove method to remove an element from the set
print(collection1)

#union #combines both set values and return new
collection2={1,2,3,4,5,6}
print(collection1.union(collection2))

#intersection (combines (common) values and returns new)
collection3={1,2,3,4,5,6,7,8}
print(collection2.intersection(collection3))

#pop (remove a random element from the set)
collection1.pop() #remove a random element from the set
print(collection1)

#clean
collection1.clear()
print(collection1)
print(len(collection1))
