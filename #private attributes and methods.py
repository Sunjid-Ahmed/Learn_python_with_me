#private attributes and methods
class Account:
    def __init__(self, acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)    

acc1=Account(12345, 'pass123')

print(acc1.acc_no)
print(acc1.reset_pass()) # Output: pass123 