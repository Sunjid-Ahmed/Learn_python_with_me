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