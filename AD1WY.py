# my_list = [34,7,32,32,5,2]
# def part(arr,low,high):
#     pivot= arr[high]
#     i = low-1
#     for j in range(low,high):
#         if arr[j]<=pivot:
#             i=i+1
#             (arr[i],arr[j])=(arr[j],arr[i])
#     (arr[i+1],arr[high])= (arr[high],arr[i+1])
#     return i + 1
# def quicksort(arr,low,high):
#     if low < high:
#         pi=part(arr,low,high)
#         quicksort(arr,low,pi)
# data=[7,8,98,2,1]
# print(data)
# size=len(data)
# quicksort(data,0,size-1)
# print(data)




# import array
# arr=array.array("i",[1,2,3])
# print(arr)

import array as arr
arr = arr.array('i',[1, 2, 3])
for i in range(len(arr)):
    print("Element %d is at position: %d"%(arr[i],i))
print("\nElements are accessed using index numbers")
try:
    x=arr[5]
except IndexError:
    print("Index Error: list assignment index out of range")
