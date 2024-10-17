# class BankAccount:
#     def __init__(self, name):
#         self.__name = name
#         self.balance = 0.0
#     def __str__(self):
#         return self.__name +', $' + '{:.2f}'.format(self.balance)

#     def deposit(self, amount):
#         self.balance = self.balance + amount

#     def withdraw(self, amount):
#         if(0 <= amount <= self.balance):
#             self.balance -= amount
            
class BankAccount:
    def __init__ (self,name):
        self.__name = name
        self.__balance = 0

    def _name(self):
        return self.__name

    def _balance(self):
        return self.__balance

    def deposit(self, amount):
        if(amount >= 0):
            self.__balance += amount

    def withdraw(self,amount):
        if(0 <= amount <= self.__balance):
            self.__balance -= amount

    def __str__(self)->str:
        return self.__name +', $' + str(self.__balance)


b = BankAccount("abc")
b.deposit(190)
b.withdraw(50)
print(b)

