info={
    "key":"value","name":"sunjid","id":728,"fav_subject":"chemistry","is_adult":True,"what":None,
    "subject":["python","java","javascript"],"topics":("dict","set")
    }

print(type(info["is_adult"]))
print(type(info["what"]))
print(type(info["fav_subject"]))
print(type(info["id"]))
print(type(info["name"]))
print(type(info["topics"]))
print(type(info["subject"]))
print(info)
info["fav_subject"]="physics"
print(info["fav_subject"])
info["surname"]="ahmed"
print(info["subject"])
print(info["topics"])
print(info)
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

#null dictionary

null_dict={}
null_dict["name"]="sunjid"
print(null_dict)


#nested dictionary

student={
    "name":"sunjid",
     "subject":{
        "phy":93,
        "chem":94,
        "math":95,
        "bio":96
    }
}
print(student)
print(student["subject"])
print(student["subject"]["phy"])