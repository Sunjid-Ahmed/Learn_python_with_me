 #class methods

class person:
    name="anonymous"

    def changename(self,name):
        person.name=name

p1=person()
p1.changename("john")
print(p1.name)
print(person.name)


class person:
    name="anonymous"

    @classmethod
    def changename(cls,name):
        cls.name=name 

p1=person()
p1.changename("john")
print(p1.name)
print(person.name)