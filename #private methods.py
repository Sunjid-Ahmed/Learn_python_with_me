#private method

class person:
    __name="anonymous!"

    def __hello(self):
        print("hello prem!")
    def welcome(self):
        self.__hello()

person1=person()
print(person1.welcome())            