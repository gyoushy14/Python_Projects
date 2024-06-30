# # Task One 2-3
# كود جاد
class El_MktapaAccout:
    def __init__(self,itemsCheckOut):
        self.itemsCheckOut = itemsCheckOut
    def CheckOutItem(self):
        if self.itemsCheckOut == False:
            print("Item is not Available")
        else:
            print("Item is Available")
    def ReturnItem(self):
        self.itemsCheckOut = True
class ElMktapaPfloos(El_MktapaAccout):
    def __init__(self,itemsCheckOut):
        super().__init__(itemsCheckOut)
    def ReturnItem(self,Days):
        if Days >= 3:
            print("you must pay 0.50$ ")
            self.itemsCheckOut = True
        else:
            self.itemsCheckOut = True
GadAcc = El_MktapaAccout(False)
GadAcc.ReturnItem()
GadAcc.CheckOutItem()
#     # HELLO MY BROTHER

# -----------------------------------------------------------------------------------------------------

# TAsk A:

class BankAcouunt:
    def __init__ (self , balance):
        self.balance = balance
        print(f"Your Balance now is {self.balance}$")
    def deposite(self , give):
        self.balance = self.balance + give
        print(f"Your balance now is about {self.balance}$ ")
    def withdraw(self , take):
        self.balance = self.balance - take
        print(f"you had take {take}$ now remain {self.balance}$")
Toto = BankAcouunt(3000)
Toto.deposite(580)
Toto.withdraw(2000)
class ChekingAcouunt(BankAcouunt):
    def __init__(self,balance):
        super().__init__(balance)
    def withdraw(self):
        super().withdraw()

# -----------------------------------------------------------------------------------------------------
# TASK 2
# list1 = []
# for i in range(2000,3201):
#     if i%7 == 0 :
#         if i%5  != 0 :
#             list1.append(i)
# print(list1)

# -----------------------------------------------------------------------------------------------------

class student:
    def __init__(self,name,age,grades):
        self.name=name
        self.age=age
        self.grades=grades
    def getname(self):
        return f"name is{self.name}"
    def getage(self,age):
        self.age=age
        return f"age is{self.age}"
    def getgrades(self,grades):
        self.grades=grades
        return f"grades are{self.grades}"
    def getaverage(self):
        return f"average is{sum(self.grades)/len(self.grades)}"
final=student("John",24,[96,85,100])
print (final.getname("John"))
print (final.getage(17))
print (final.getaverage())







