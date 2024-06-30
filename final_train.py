q=[(2,"E"),(3,"a")]
def quick(q):
    if len(q) <= 1:
        return q
    else:
        piv = q[0]
        less = [i for i in q[1:] if i[0]<piv[0] or (i[0]==piv[0] and i[1]>piv[1])]
        big = [i for i in q[1:] if i[0]>piv[0] or (i[0]==piv[0] and i[1]<piv[1])]
        return quick(less) + [piv] + quick(big)
print(quick(q))


# ---------------------------------------------------------
# SELECTION SORT

sel_li = [34,56,21,1,3,2]
def selection (sel_li):
    for i in range(len(sel_li)):
        current = i 
        for j in range(i+1 , len(sel_li)):
            if sel_li[current] > sel_li[j]:
                current=j
            sel_li[i] , sel_li[current] = sel_li[current] , sel_li[i]
    return sel_li
print(selection(sel_li))

# ---------------------------------------------------------

# Merge sort

merge_list=[5,3,4,1,2]
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


def mergaia(merge_list):
    if len(merge_list)>1:
        mid = len(merge_list)//2
        left = merge_list[:mid]
        right = merge_list[mid:]
        mergaia(left)
        mergaia(right)
        i=j=k=0
        while i<len(left) and j < len(right):
            if left [i] < right[j]:
                merge_list[k] = left[i]
                i+=1
            else:
                merge_list[k] = right[j]
                j+=1
            k+=1
        while i<len(left):
                merge_list[k] = left[i]
                i+=1
                k+=1
        while j < len(right):
            merge_list[k] = left[j]
            j+=1
            k+=1
            
mergaia(merge_list)
print(merge_list)







merge_list = [9,3,7,1,8,3,2]
def mergaia (merge_list):
    if len(merge_list)>1:
        mid = len(merge_list)//2
        left = merge_list[:mid]
        right= merge_list[mid:]
        mergaia(left)
        mergaia(right)
        i=j=k=0
        while i < len(left) and j < len (right):
            if left[i] < right[j]:
                merge_list[k]=left[i]
                i+=1
            else:
                merge_list[k]=right[j]
                j+=1
            k+=1
        while i < len(left) :
            merge_list[k]=left[i]
            i+=1
            k+=1
        while j < len (right):
            merge_list[k]=right[j]
            j+=1
            k+=1
mergaia(merge_list)
print(merge_list)



q=[(2,"E"),(3,"a")]
def quick (q):
    if len(q) <=1:
        return q
    else : 
        piv = q[0]
        less= [i for i in q[1:] if i[0] < piv[0] or (i[0]==piv[0] and i[1]>piv[1])]
        big= [i for i in q[1:] if i[0] > piv[0] or (i[0]==piv[0] and i[1]<piv[1])]
        return quick(less) + [piv] + quick(big)
print(quick(q))

