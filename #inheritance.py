#inheritance
class car:
    color="black"
    @staticmethod
    def start():
        print("car started...")
    @staticmethod 
    def stop():
        print("car stopped....")

class Toyotacar(car):
      def __init__(self,name):
        self.name=name

car1=Toyotacar("fortuner")
car2=Toyotacar("prius")

print(car1.name)
print(car1.start())
print(car1.color)