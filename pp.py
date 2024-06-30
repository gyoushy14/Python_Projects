# (#) to write a comment in Python must write # or تحديد السطر و الضغط في الكيبورد على كنترول ظ

# --------------------------------------------------------------------------------------------------------------------------

# variable is container for any values , you allow give variable any name but doesnot start by number , doesnot called by built in functions in python , such as : (list , tuple , print, .............)
# you can add number for variable between words or end of words , Examples :
# name = "Ali"
# age = 17
# year=2007
# name2="Mohamed"
# age2 = 16
# year2=2008
# print(name,age,year)
# print(name2,age2,year2)

# print => is built in pythone using to appear output 
# output is result from code

# ----------------------------------------------------------------------------------------------------------------------------

# Types of data in Python 
# str => string = words
# int => integer = numbers = 1,2,3,4,5
# float =>  floating point number = 1.0, 2.5, 3.7 etc
# list => []
# dictionary => {}
# tuple => () => for methods

# ----------------------------------------------------------------------------------------------------------------------------

# \ => conctenate two lines together , Example :
# name="Mahmoud \
# Elgyuoshy"
# print(name)

# --------------------------------------------------------------------------------------------------------------------------

# \n create new line or write words in new line , Example : 
# presentation="My name is Omar\nMy age 17\nMy country is Egypt"
# print(presentation)

# --------------------------------------------------------------------------------------------------------------------------

# INDEX => ترقيم . give number for all character , start from 0 to end of the word . Example : 
# familyname="I am student in We School"
# print(familyname[0])
# print(familyname[1])
# print(familyname[2])
# print(familyname[3])

# if you need start from end == -1 , not 0 ,  Example :
# familyname2="I am student in We School"
# print(familyname2[-1])
# print(familyname2[-2])
# print(familyname2[-3])
# print(familyname2[-4])

# if you want specify start and end of index , we using : , Example : 
# familyname3="I am student in We School"
# print(familyname3[2:7])  # will start from 2 and stop before 7 , all of programming language do it   
# print(familyname3[0:9]) # will start from 0 and stop before 9 , all of programming language do it  
# print(familyname3[1:10]) # will start from 1 and stop before 10 , all of programming language do it  

# --------------------------------------------------------------------------------------------------------------------------

# STRING METHODS : lower() , islower() , upper() , isupper() , capatlize() , tittle() , split() , rsplit()

# lower() => make all characters small , islower() => ask is all carachters small ? , Examples : 
# x = 'NAME'
# print(x.lower())
# print(x.islower())

# --------------------------------------------------------------------------------------------------------------------------

# upper() => make all characters capital  , isupper()  => ask is all carachters capital ? , Examples : 
# A = 'eygpt'
# print(A.upper())
# print(A.isupper())

# --------------------------------------------------------------------------------------------------------------------------

# capatlize() => make first carachter capital , Example : 
# r='mahmoud mohamed'
# print(r.capitalize())

# --------------------------------------------------------------------------------------------------------------------------

# tittle() => make first carachter words capital , Examples : 
# z="python is on programming language";print(z.title())

# --------------------------------------------------------------------------------------------------------------------------

# split() => convert type of data from STRING to LIST. You can write at bracket of split method , it allow you add 2 values 
# First_value : specify what is be space between words , such as : (,) , (_) , (any word) 
# Second_value : how many of words will execute method on it  
#   , Examples :  
# prog_lan="Html Css Js Php Py"
# prog_lan2="Html_Css _Js_Php_Py"
# prog_lan3="Html,Css,Js,Php,Py,C++"
# print(prog_lan.split()) 
# print(prog_lan2.split("_",2)) 
# print(prog_lan3.split(",",3)) 
# rsplit() === SPLIT() but from right
# print(prog_lan.rsplit()) 
# print(prog_lan2.rsplit("_",2)) 
# print(prog_lan3.rsplit(",",3))

# --------------------------------------------------------------------------------------------------------------------------

# to know type of data  in python use "type()" function , Example:
# a = 5;d=3.2;z="ahmed";con=9j
# print(type(a),type(d),type(z),type(con))

# --------------------------------------------------------------------------------------------------------------------------

# print("years : " + str(7+6))
# print(int(2.2));# print(complex(2.2))

# --------------------------------------------------------------------------------------------------------------------------


# to invoke math library => from math import * =>
# from math import *
# print(round(9.1));print(ceil(8.4));print(floor(9.7));print(sqrt(100));print(pow(2,3))
# print("-------------------------------------------------------------")
# print(ceil(3.4));print(ceil(3.7))
# abs convert from - to + 
# print(abs(-12))
# min to print mini number , max to print maxi number
# print(max(7,15));print(min(7,15))

# --------------------------------------------------------------------------------------------------------------------------


# name= input("Enter your name : ")
# num2= input("Enter your Number : ")
# print("Hello "+ name+" Your Number Is "+num2)

# num55=float(input("Enter number"))
# num5= float(input("Enter number"))
# print(num55+num5)

# --------------------------------------------------------------------------------------------------------------------------

# name= input("What`s your nickname ? \n ")
# des=input("What`s Channel about ? \n")
# print(name ,"with" , des )


a=str(8765)
# print(type(a))