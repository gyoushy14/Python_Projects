# # class product:
# #     def __init__(self,name,quantity,price,product_id):
# #         self.name = name
# #         self.quantity = quantity
# #         self.price = price
# #         self.product_id=product_id
# #     def dis_info(self):
# #         pass
# # class book (product):
# #     def __init__(self,name,quantity,price,product_id,isbn):
# #         super().__init__(name,quantity,price,product_id)
# #         self.isbn = isbn
# #     def dis_info(self):
# #         print( f"Book : {self.name}\nPrice : {self.price}\nProduct id : {self.product_id}\nISBN : {self.isbn}")
# # class clothes(product):
# #     def __init__(self,name,quantity,price,product_id,size):
# #         super().__init__(name,quantity,price,product_id)
# #         self.size = size
# #     def dis_info(self):
# #         print( f"Clothe : {self.name}\nPrice : {self.price}\nProduct id : {self.product_id}\nSize : {self.size}")
# # class Elecotronics(product):
# #     def __init__(self,name,quantity,price,product_id,warranty):
# #         super().__init__(name,quantity,price,product_id)
# #         self.warranty = warranty
# #     def dis_info(self):
# #         print( f"Clothe : {self.name}\nPrice : {self.price}\nProduct id : {self.product_id}\nwarranty period : {self.warranty}")   

# # ______________________________________________________________________________________________________________________#

merge_list=[5,3,4,1,2]
# merge_list.sort()
def merge_sort(merge_list):
    if len (merge_list) > 1:
        mid = len(merge_list) // 2 
        left= merge_list[ :mid]
        right=merge_list[mid:]
    # recursion
        merge_sort(left)    
        merge_sort(right)
    # merge
        i=0
        j=0
        k=0 #  i => index left , j=>  index right , k => index megred
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merge_list[k] =left[i]
                i+=1
            else:
                merge_list[k]=right[j]
                j+=1
            k+=1
        while i < len(left):
                merge_list[k]=left[i]
                i+=1
                k+=1
        while  j < len(right):
            merge_list[k]=right[j]
            j+=1
            k+=1
merge_sort(merge_list)
print(merge_list)

# # -------------------------------------------------
# # import array as r
# # def get(n):
# #     return sum(range(10,21)) - sum(list(n))
# # arr=r.array([10,11,12,13,14,16,17,18,19,20])
# # for i in range(len(arr)):
# #     print(arr[i])
# #     print(get(arr))
# # arr=r.array([10,11,12,13,14,15,16,17,18,19,20])
# # for i in range(len(arr)):
# #     print(arr[i])
# #     print(get(arr))
# # -----------------------------------------
# # # WORKSHOP ARRAY
# # li = [1,2,4,5,67,9]
# # print(li[0])
# # print(li[-1])
# # # tot=sum(li)
# # suum=0
# # for i in li:
# #     suum+=i
# #     print(suum)
# # # print(tot)
# # # find small and lg
# # sma=li[0]
# # lg=li[0]
# # for i in li :
# #     if i < sma:
# #         sma=i
# #     if i > lg:
# #         lg=i
# # print()
# # print("_"*123)
# # print()
# # print(lg,sma)
# # ---------------------------------------------------------------------------------------------------
# print()
# print("_"*123)
# print()
# ARR1=[1,2,4,5,6]
# ARR2=[1,2,3,4,5,6]
# ff=sum(ARR2) - sum(ARR1)
# ARR1.append(ff)
# ARR1.sort()
# print(ff)
# print(ARR1)
# # ---------------------------------------------------------------------------------------------------
