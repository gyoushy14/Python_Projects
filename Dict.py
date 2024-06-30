# [1] Dictionary 
# [2] to create dictionary , use curly braces {} and assign key-value pairs.
# [3] Dictionary contains key and values . unique keys but can have duplicate values.
# [4] must seperate between key bt comma #,#
# [5] Mutable  data type : Can be changed , deleting and adding after creation.
# [6] Dictionary can have diffrent data types => nums , str , bool ... .
# [7] Dictionary unordered.

Ahmed={
    "name" : "Ahmed" ,
    "age" : 16 ,
    "gender" : "male",
    "email" : "waleed@gmail.com",
    "money" : "1000000$",
    "Properties" : ["3bkary" , "Geinus" , "Programer" ,  "Student" , 7.5],
    "langs":{
        "Html" : "Structure of web pages" ,
        "CSS" : "To design web",
        "JS": "Makes websites interactive" ,
        "Python":"Used in Data Analysis and AI",
    },
    "grade" : 91.88,
}

# accessing
# print(Ahmed)
# print(Ahmed["name"])
# print(Ahmed.get("name"))
# print(Ahmed.keys()) # View all Keys8
# print(Ahmed.values) # View all values
# print(Ahmed["Properties"][2]) # Accessing list inside the dict
print(Ahmed["langs"]["CSS"]) # Accessing Dict inside the dict
# print(len(Ahmed["Properties"])) # Number Of Elements In List
# print(len(Ahmed["Properties"][2])) 

# METHODS
#  [1] Clear to remove all items
# Ahmed.clear()
# print(Ahmed)

#  [2] update method is used to add new kay value pair or update existing one
# Ahmed["langs"].update({"city" : "Suez"})
# print(Ahmed["langs"])
# Update or add key without update() maethod
# Exist condition to modify on dict => must Create dict before modify =>
# user={}
# Ahmed["country"] = "Egypt"
# Ahmed["money"] = 1
# user["name"]="JO"
# print(Ahmed)
# print(user)

# Allitems=Ahmed.items()
# print(Allitems)
# print("\n")
# print("######################################################################################################################################################")
# Letters=("A" , "B" , "C" , "Z" )
# V_Letters=("")
# print(dict.fromkeys(Letters,V_Letters))

# print("jjj")
# b = ["som3a","hasan","Abdala"]
# x = b.remove("som3a")
# print(x)
# print(b)