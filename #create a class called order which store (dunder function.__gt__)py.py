#create a class called order which stores item and its price
#use dunder function __gt__() to convet that:
#order1>order2 if price of order1>price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, or2):
        return self.price > or2.price
        
or1=Order("Apple", 20)
or2=Order("Banana", 15)

print(or1 > or2) #True, as Apple's price is greater than Banana's price