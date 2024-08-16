info={
    "key":"value","name":"sunjid","id":728,"fav_subject":"chemistry","is_adult":True,"what":None,
    "subject":["python","java","javascript"],"topics":("dict","set")
    }
#keys
print(info.keys())
print(list(info.keys()))
#length
print(len(list(info.keys())))

#values
print(info.values())
print(list(info.values()))

#items
print(info.items())
print(list(info.items())) #convert into list
pairs=list(info.items())
print(pairs[0]) #individual access

#get any item(info.get("key"))

print(info["name"]) #show error if the key is not present
print(info.get("name")) #no error if the key is not present but show None

#update
info.update({"city":"delhi","age":23,"name":"monira"})
print(info)
