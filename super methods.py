class car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("car started...")
    @staticmethod 
    def stop():
        print("car stopped....")

class Toyotacar(car):
      def __init__(self,name,type):
        self.name=name
        super().__init__(type)
        super().start()
        super().stop()



car1 =Toyotacar("prius", "electric")
print('The car is an',car1.type,'car!')
print(car1.name)