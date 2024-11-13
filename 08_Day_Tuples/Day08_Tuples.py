###Tuples
'''A tuple is a collection of different data types which is ordered and unchangeable (immutable). Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). Unlike list, tuple has few methods. Methods related to tuples:

tuple(): to create an empty tuple
count(): to count the number of a specified item in a tuple
index(): to find the index of a specified item in a tuple
operator: to join two or more tuples and to create a new tuple'''

# Empty tuple
# # syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()
print(empty_tuple)

# Tuple with initial values
tup=("item1","item2" ,"item3" )
print(tup)
fruits=('banana', 'mango','apple')
print(fruits)
print(len(fruits))

# Accessing Tuple Items: Positive Indexing Similar to the list data type we use positive or negative indexing to access tuple items.
fruits=('banana', 'mango','apple')
print(fruits[0:2])

# Negative indexing: Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last and the
fruits=('banana', 'mango','apple','grapes','orange')
print(len(fruits)-1)
last_index =len(fruits) - 1
print(last_index)


# Slicing tuples: We can slice out a sub-tuple by specifying a range of indexes where to start and where to end in the tuple, the return value will be a new tuple with the specified items.
# Range of Positive Indexes:
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4] 
print(all_items)            # all items
all_items = tpl[0:]    
print(all_items)          # all items(because python interptiter assume end value as end of out input or tup)
middle_two_items = tpl[1:3]   
print(middle_two_items)   # does not include item at index 3

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]   
print(all_fruits)      # all items
all_fruits= fruits[0:]     
print(all_fruits)      # all items
orange_mango = fruits[1:3] 
print(orange_mango)      # doesn't include item at index 3
orange_to_the_rest = fruits[1:]
print(orange_to_the_rest)

# Range of Negative Indexes:
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]    
print(all_items)     # all items
middle_two_items = tpl[-3:-1] 
print(middle_two_items) # does not include item at index 3 (-1)

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:] 
print(all_fruits)   # all items
orange_mango = fruits[-3:-1] 
print(orange_mango) # doesn't include item at index 3
orange_to_the_rest = fruits[-3:]
print(orange_to_the_rest)


# Changing Tuples to Lists: We can change tuples to lists and lists to tuples. Tuple is immutable if we want to modify a tuple we should change it to a list.
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)
print(type(lst))

# EX:
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')

# checking an Item in a Tuple: We can check if an item exists or not in a tuple using in, it returns a boolean.
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment

# joining Tuples:We can join two or more tuples using + operator
# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables

# Deleting Tuples: It is not possible to remove a single item in a tuple but it is possible to delete the tuple itself using del.
# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits


# Exercises: Level 1
#1) Create an empty tuple
empty_tpl =()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers =("vishal","aniket","harshal")
sisters =("vaishanvi","reshma")

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)

# How many siblings do you have?
print(len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family =list(siblings)
family.extend(["rutik","baliram","pramila"])
family_members =tuple(family)
print(family_members)
# print(family)

## Unpack siblings and parents from family_members

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruit =('banana', 'orange', 'mango', 'lemon')
animal_products = ('catfood','dogfood',)
vegetables = ('ladyfinger','brinjle','tomato')
food_stuff_tp = fruit + animal_products + vegetables
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt =list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the first three items and the last three items from food_staff_lt list
mid_index = len(food_stuff_lt) // 2
print(mid_index)
middle_item = food_stuff_lt  [mid_index - 1 : mid_index + 1] if mid_index % 2 ==0 else food_stuff_lt [mid_index + 1]
print(middle_item)

# Delete the food_staff_tp tuple completely
del food_stuff_tp
