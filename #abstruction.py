#abstruction
class car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self): 
        self.clutch=True
        self.acc=True
        self.brk=True
        print("car started...")

car1=car()
car1.start()            