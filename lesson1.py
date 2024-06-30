# List

# 1. Create a List of the first 10 even numbers
even_numbers = [x for x in range(2, 21, 2)]
# 2. List Append: Appends the square of each number from 1 to 5 to an empty list
squares = []
for x in range(1, 6):
    squares.append(x**2)
# 3. List Slicing: Slicing a list to only include elements from the third to the seventh position
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sliced_list = sample_list[2:7]
# 4. List Comprehension: Create a list of the cubes of the first 10 natural numbers
cubes = [x**3 for x in range(1, 11)]
# 5. Remove Duplicates: Remove duplicates from a list without using set
duplicate_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []
for x in duplicate_list:
    if x not in unique_list:
        unique_list.append(x)
# 6. Find Common Elements: Find the common elements between two lists without using set operations
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = [x for x in list1 if x in list2]
print(common_elements)

# Dictionaries

# 7. Create a Dictionary
square_dict = {i: i*i for i in range(1, 6)}

#8.  Merge Dictionaries
dict1 = {'a': 100, 'b': 200}
dict2 = {'x': 300, 'y': 200}
merged_dict = {**dict1, **dict2}

# 9. Key Existence
def check_key_existence(d, key):
    return key in d

# 10. Extract Unique Values
list_of_dicts = [{'v': 1}, {'v': 2}, {'v': 1}, {'v': 3}, {'v': 4}, {'v': 3}]
unique_values = set(val for dic in list_of_dicts for val in dic.values())

# Tuples
# 11. Swap Values
def swap_first_last(t):
    if len(t) > 1:
        return t[-1:] + t[1:-1] + t[:1]
    return t

# Sets
# 12. Create a Set of the first 5 prime numbers
prime_numbers = {2, 3, 5, 7, 11}

#13. Set Operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)

# 14. Symmetric Difference
symmetric_difference = (set1 | set2) - (set1 & set2)

# 15. Subset Check
def is_subset(set_a, set_b):
    return set_a.issubset(set_b)

# 16.
original_dict = {'item1': 150, 'item2': 200, 'item3': 50, 'item4': 120}

# Filtering dictionary to include items where the value is greater than 100
filtered_dict_corrected = {key: value for key, value in original_dict.items() if value > 100}

filtered_dict_corrected
print(filtered_dict_corrected)