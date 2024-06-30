# OOP => OBJECT ORINTED PROGRAMMING 
# CLASS IS BLUEPRINT OR CONSTRUCTOR OF OBJECT , PROVIDE FOR YOU CREATE INSTANCE /OBJECT FROM IT.
# CLASS DEFIND WITH KEW class 
# __INIT__ METHOD IS INITIALIZE DATA FOR OBJECT . INIT BELONG TO DUNDOR OR MAGIC METHOD
# 
# To create Class method for class we use @classmethod decorator 
# It take Cls parameter which represent the class itself
# Static methods : it takes no parameter , but you can add para
# To create static method in python just simply define a normal function inside your class and put @staticmethod decorator on top 
# To accessing on it => classname.method()

# --------------------------------------------------------------------------------------------------------------

# class cars:
#     def __init__(self , color , model , speed ):
#         self.name="BMW"
#         self.color=color
#         self.model=model
#         self.speed=speed
#     def speed_of_car(self):
#         return f"{self.name} is a good car and it can run with {self.speed} km/h "
# car_obj1=cars("Black","X1 SUV",300)
# print_method=car_obj1.speed_of_car()
# print(print_method)

# --------------------------------------------------------------------------------------------------------------
# class form:
#     count_of_user=0
#     @classmethod
#     def p(Cls):
#         print(f"We have {Cls.count_of_user} users in our system")
        
#     def __init__(self , fname , lname , password , phone , gender):
#         self.fname = fname
#         self.lname=lname
#         self.password=password
#         self.phone=phone
#         self.gender=gender
#         form.count_of_user+=1 #after create obj will increase 1
#     def full_name(self):
#         z=f"Your Full Name Is :{self.fname} {self.lname} "
#         print(z)
#     def show_pass(self):
#         print(f"Your password is : {self.password}")
#     def he(self):

#         if self.gender=='male':
#             print(f"Hello MR {self.fname} {self.lname}")
#         elif  self.gender=='female':
#             print(f"Hello MRS {self.fname} {self.lname}")
#         else:
#             print("you  are not define your gender . you are just 3bd")

# user1=form(input("Enter your first name : "),input("Enter your last name : "),input("Enter Your Password : "),input("Enter Your Phone Number : ") , input("Enter Your Gender : ").lower())
# user2=form(input("Enter your first name : "),input("Enter your last name : "),input("Enter Your Password : "),input("Enter Your Phone Number : ") , input("Enter Your Gender : ").lower())
# user1.full_name()
# user1.show_pass()
# user1.he()
# user2.full_name()
# user2.show_pass()
# user2.he()
# form.p()
# print("\n");print("="*150)
# --------------------------------------------------------------------------------------------------------------

# INHERTANCE

# def greet():
#     print("Suiiiiiiiiiii")

# class staduims:
#     stad="audince"
#     def __init__(self,Santiago,campno , anfield , old_trafford):
#         self.Santiago= Santiago
#         self.campno= campno
#         self.anfield= anfield
#         self.oltrafford=old_trafford
#     def have(self):
#         print(f"Santiago : {self.Santiago}\n")
#         print(f"campno : {self.campno}\n")
#         print(f"anfield : {self.anfield}\n")
#         print(f"oldtrafford : {self.oltrafford}\n")
#     def gh(self):
#         print("suiiii")

# class stad(staduims):
#     def __init__(self, Santiago, campno, anfield, old_trafford):
#         super().__init__(Santiago, campno, anfield, old_trafford)
#     def gh(self):
#         print("messiii")
#     def people(self):
#         print(f"\n{self.Santiago} club has a lot of audience")
# teams=staduims("Real madrid" , "Barcalona" , "Liverpool" , "manu")
# team=stad("Real madrid 17" , "Barcalona 17" , "Liverpool 17" , "manu 17")
# #teams.have()
# team.have()
# print("\n")
# teams.have()
# staduims.gh()
# print("\n");print("="*150)
# --------------------------------------------------------------------------------------------------------------

# def greet():
#             print("ياشبااااااب")
# class greters :
#     def __init__(self,tit):
#         self.tit=tit
#     def greet(self):
#         print(f"{self.tit} just 3bota")
# gr=greters(input("Enter name : "))
# gr.greet()
# greet()

# print("\n");print("="*150)
# --------------------------------------------------------------------------------------------------------------

# class person:
#     address="elsayedhashem"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# a=person("Adwy" , 199)
# e=person("Adwy" , 19)
# print(a.age)
# print(e.name)
# print(a.name)
# print(person.address)
# print("\n");print("="*150)
# --------------------------------------------------------------------------------------------------------------
# incresee =+100
# decresee =-100
# class car :
#     def __init__(self,speed):
#         self.speed=speed
#     def inc(self):
#         self.speed=incresee
#         print(f"The speed of car is {self.speed}")
#     def dec (self):
#         self.speed =decresee
#         if self.speed<0:
#             self.speed=0
#             print(f"{self.speed}")
# obg=car(60)
# obg.inc()
# obg.dec()
# obg.decrease()
# print(obg.speed)

# --------------------------------------------------------------------------------------------------------------

# class we:
#     school="WE"
#     def __init__(self,name,id):
#         self.n=name
#         self.id=id
#     def stu(self):
#         print(f"name : {self.n}")
#         print(f"id : {self.id}")
#         return we.school==input("School : ")
# kob=we("ali",13)
# ko=we(input("Enter your name : "),input("Enter your ID : "))
# ko.stu()

# --------------------------------------------------------------------------------------------------------------

# class T:
#     def __init__(self,C):
#         self.C=C
#     def chan(self):
#      print(self.C * (5/9) + (32))
# onm=T(187)
# onm.chan() 

# # --------------------------------------------------------------------------------------------------------------

# ENCAPSULATION 
# _ATT => protected property => self._name => using of it in class only

# __ATT => privte property => self.__name => using in the same creation class , i cannot modify on it 

# class peo:
#     def __init__(self , name,age):
#         self.__name=name # private attribut
#         self._age=age #protected attibute
#     def k(self):
#         return print(f"Name is {self.__name} and Age is {self._age}")

# use=peo("jo" , 40)
# use.__name="ko"
# print(use.k())
# print(use._age)
# print(use._peo__name)

# --------------------------------------------------------------------------------------------------------------

# GETTERS , SETTERS 
# class Peoples:
#     def __init__(self , n , a):
#         self.n=n
#         self.a=a
#     def  set_name(self , new):
#         self.n=new
#     def get(self):
#         return self.n
# ojb=Peoples("kj","Male")
# print(ojb.get())
# ojb.set_name("joe")
# print(ojb.get())

# --------------------------------------------------------------------------------------------------------------

#  class book:
#      def __new__(Cls,author , pages):
#          if pages >1000:
#              print(False)
#          else:
#              print(True)
#          return super().__new__(Cls)
#      def __init__(self , author , pages):
#          self.au=author
#          self.pa=pages
#      def MN(self):
#          return f"Exist in book {self.pa} , this book created by {self.au}"
#  user1=book("JO" , 1002)
#  user1.MN()

# # --------------------------------------------------------------------------------------------------------------
# class VI : 
#     def __init__(self,color,wheels,eng):
#         self.color=color
#         self.wheels=wheels
#         self.is_engine=eng
#     def is_yes_no(self):
#         if self.is_engine==True:
#             print("success")
#         else:
#             print("failed")
#     def move(self):
#         if self.wheels==4:
#             print("Driving")
#         elif self.wheels==2:
#             print("pedaling")
#         elif self.wheels==0:
#             print("not exist")

# class car(VI):
#     def __init__(self,color,wheels,eng):
#         super().__init__(color,wheels,eng)
#         self.is_engine=eng
#     def speed(self):
#         print(f"High speed")
# class cdr (car):
#     def __init__(self,color,wheels,eng):
#         super().__init__(color,wheels,eng)
#         self.is_engine=eng
#     def dis(self):
#         print(f"great {self.color} ")
#     class pl:
#         def __init__(self,color,wheels):
#             super().__init__(color,wheels)
# user1=VI("red",4,True)
# user2=car("blue",2,False)
# user3=cdr("green",0,True)
# user3.is_yes_no()
# user2.is_yes_no()
# user1.move()
# user2.move()
# user3.move()
# --------------------------------------------------------------------------------------------------------------

# PROPERTY DECORATOR => any def just return value , you can convert it to property : @property

# class users:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     @property
#     def hi(self):
#         return self.age*365
# ali=users("ali",78)
# print(ali.hi)
# --------------------------------------------------------------------------------------------------------------

# 
from abc import ABCMeta , abstractclassmethod
class prog(metaclass=ABCMeta):
    @abstractclassmethod
    def run(self):
        pass

class comm(prog):
    def run(self):
        return "Hello My Future"
class net (prog):
    def run(self):
        print ("I am learning Net")
stu2=comm()
# stu3=net()
# st1=prog()
print(stu2.run())

# --------------------------------------------------------------------------------------------------------------

# class A:
#     def __init__(self):
#         self.b=5
#         self.b=b+1

#     def display(self):
#         print(self.b)
# obj=A("Hello")
# print (obj.b)

# --------------------------------------------------------------------------------------------------------------

# class R:
#     def __init__(self,name="ali"):
#         self.name = name
# class d(R):
#     def __init__(self, ne="ahmed"):
#         super().__init__()
#         self.ne=ne
# def l():
#     obj=d()
#     print(obj.name , obj.ne)
# l()

# --------------------------------------------------------------------------------------------------------------

# class demo:
#     def __new__(self):
#         self.__init__(self)
#         print("NEW invoke1")
#     def __init__(self):
#         print("init__() invoked")
# class driv:
#     def __new__(self):
#         print("NEW invoke2")
#     def __init__(self):
#         print("init__() invoked2")
# ong2=driv()
# obj1=demo()

# --------------------------------------------------------------------------------------------------------------

# class name:
#     def dis(Self):
#         print("hello")
# class k(name):
#     pass
# ong=name()
# ong.dis()
# a=name
# print(name.__name__)

# --------------------------------------------------------------------------------------------------------------

# class sh:
#     def __init__(self,side):
#         self.side=side
#     def get(self):
#         return self.side
#     def seti(self,v):
#         if v>0:
#             print("true")
#         else:
#             print(False)
# k=sh(4)
# k.seti(-1)
# print(k.get())

