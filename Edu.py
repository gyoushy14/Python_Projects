# List is data type in PY 
# we can define list by use []
# Lists are mutable => add,delete,modify
# Lists are ordered collection of items
# List Items not unique 
# Seperate between items By COMMA = ,
# List can have diffrent data types => nums , str , bool ...
friuts=["apple" , "banana", "orange" , 14 , 1.5 ,"peach" ,"watermelon" , "apple"]

footballers=["Cr7" , "messi" , "Zlatan" , "nemar"]

nums=[10,20,30,40,50,60]
nums.sort()
# print(len(nums))
# nums.sort(reverse=True)
print(len(nums))
# print(nums,nums[2:4])
# ordered ###############
# print(friuts)
# print(friuts[2])
# print(friuts[-1])
# i can change items in list by index :
# friuts[0]="mango"
# friuts[2:5]=["grapes","kiwi","ali"]
# print(friuts)

# if me want print 3 or 4 items , me can use slice :
# print(friuts[1:4]) #start from 1 and stop before 4

# APPEND is method adding at the end of list
# footballers.append("Halland")
# footballers.append(friuts)
# print(footballers[5][3])

# REMOVE is method to delete item from list by value
# footballers.remove("messi")

# Sort is method to sort the list
# footballers.sort()

# reverse is method to reverse the list
# footballers.reverse()

# Clear is method to remove all items from list 
# footballers.clear()

# Count is method  that return how many times a specific value appear in list
# print(friuts.count("apple"))

# Insert is method  that insert new item into specific position by index
# friuts.insert(3,"grapefruit")
# print(friuts)

# Pop is method that removing an item by its index and returning it 
# nums.pop(2)
# # nums.remove(3)
# print(nums)
# print(friuts)

# Del is keyword used for deleting by index in list
# del  nums[0]
# print(nums)

# print(footballers)



start = 2000
end = 3200
arr=[]
for i in range(start,end +1):
    if i % 7 == 0 and i % 5 != 0:
        arr.append(i)
print(arr)