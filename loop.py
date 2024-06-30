# ani=["lion" , "tiger" , "zebra" , "rabbit" , "cat"]
# for i in ani :
#     print(i)
# print("-"*99)

# ---------------------------------------------------------------------------------------------------------

# for x in ani:f
#     if x=="lion":
#         print(f"{x} : is my fav animal")
#     else:
#         print(f"{x} : just animal")

# ---------------------------------------------------------------------------------------------------------

nums=[44,3,22,6,7,9,87,78]
# for b in nums :
#     if b%2==0:
#         print(f"{b} : is even number")
#     elif b%2 !=0:
#         print(f"{b} : is odd number")

# ---------------------------------------------------------------------------------------------------------
# RANGE(stop)
# for s in range(4,9): #rang(start,stop)
#     print(s)

# for z in range(9,30,2): #  rang(start,stop,step)
#     print(z)

# for c in range(7): # will start from 0 and stop before 7
#     print(c) 
    
# ---------------------------------------------------------------------------------------------------------
    
s1={3,4}
s2={1,2}
s3=set()
i=0
j=0
for i in s1:
    for j in s2:
        s3.add((i,j))
        i+=1
        j+=1
    print(s3)