# def average():
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
#     num3 = float(input("Enter the third number: "))
#     num4 = float(input("Enter the fourth number: "))
#     avg = (num1 + num2 + num3 + num4) / 2.0
#     return avg # return value for def
# # return will end the function and send back a value to whoever called it

# print(average()) #this print outside of function , this call for function

# print("\n")
# -------------------------------------------------------------------------------------------
# print( "#" *80)

# def calcage(age):
#     return f"your age = {age} years old then \n {age*365} = day."
# # print(calcage(9))
# print(calcage(int(input("enter your age : "))))
# print("\n")

# print("\n")
# -------------------------------------------------------------------------------------------
# import random 
# a=random.randint(1000,9999)
# # print(a)
# # import 
# # print(pp.a)
# ini_4=int(input("Enter a 4-digit PIN code : "))
# if len(str(ini_4)) != 4:
#     print("Sorry , just 4-digit ")
# elif ini_4==a:
#     print("Perfect sir")
# else:
#     print(f"Wrong sir. the pin code is {a} ")

# -------------------------------------------------------------------------------------------

class ui :
    def __new__(Cls,stu,grade):
        Cls.stu=stu
        Cls.grade=grade
        return super().__new__(Cls) #دي ميثود ثابتة مبستخدمهاش غير في المشاريع الكبيرة 
    # طب بتعمل ايه ؟ دي ميثود ثابتة على الكلاس و تعود عليه ممكن تقول كدا عملنا كلاس صغير على الضيق جوة كلاس
    
    def dis(Cls):
        pass
    def __init__(self,age,name):
        self.age=age
        self.name=name

# -------------------------------------------------------------------------------------------

