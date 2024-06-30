# class student : 
#     def __init__(self , name , age , grade):
#         self.n=name
#         self.a=age
#         self.g=grade
#         self.g2=78
#     def grade(self):
#         print(f"The student {self.n} is of {self.g} grade")
#     def update(self):
#         print(f"The student {self.n}  has been updated with new grade : {self.g2}. ")
    
# obj1=student("JO" , 18 , 80)
# obj2=student("ALI" , 17 , 90)
# obj1.grade()
# obj2.grade()
# obj2.update()
# obj1.update()

# class teacher (student):
#     def __init__(self , name , age , grade ):
#         super().__init__(name,age,grade)
#     def update(self):
#         print(f"The teacher {self.n} has been updated grade for student : {self.g2}. ")
# teacher1=teacher("MARK",35,60)
# teacher1.grade()
# teacher1.update()

# class book:
#     def __init__(self , tittle , author , d):
#         self.tittle=tittle
#         self.author=author
#         self.exist_book=d
#     def checkout(self):
#         if  self.exist_book==False:
#             print(f"{self.tittle} by {self.author} has been checked out")
#     def  return_book(self):
#         if  self.exist_book==True:
#             print( f"{self.tittle} by {self.author} has been returned")

# user1=book("GHOST" , "ahmed",True)
# user2=book("CR7" , "ALI",False)
# user1.checkout()
# user2.checkout()
# user1.return_book()
# user2.return_book()