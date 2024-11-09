# Lists(lists are mutable=can change strings are immutable= can not change )
# there are 4datatypes in python 
# 1)Lists
# 2)tuple 
# 3)dictionary
# 4)set

# Lists is an  collection which is ordered and changeable(modifiable). Allows duplicate members.
# In Python we can create lists in two ways:

# Using list built-in function
# syntax
lst = list()
empty_list = list() # this is an empty list, no item in the list
print(len(empty_list)) # 0

# Using square brackets, []
# syntax
lst = []
empty_list = [] # this is an empty list, no item in the list
print(len(empty_list)) # 0

# In lists we store various types of elements like innteger, float, strings, Ex:
marks =[84, 57, 66, 53, 69]
student=[55,"rutik",66,"barde"]   # in lists we can make chages in lists or change the value in lists 

student[1]="Rutikkkkkkk"  # here we modified rutik=Rutikkkkkkk
print(student)

# Accessing List Items Using Positive Indexing
# We access each item in a list using their index. A list index starts from 0


fruits=["mango","banana","orange","lemon"]
first_fruit=fruits[0]
print(first_fruit)  #Output=mango cause counting starts from o,1,2,3.....



# Accessing List Items Using Negative Indexing
# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item.


fruits=["mango","banana","orange","lemon"]
last_fruit=fruits[-1]
print(last_fruit)

#list methods 
marks =[1, 3, 4, 2]

# list.append(4) #this adds one element at the end Ex:
marks.append(5)
print(marks)

# list.sort( ) #this sorts in ascending order
marks.sort()
print(marks)


# list.sort( reverse=True ) #sorts in descending order
marks.sort(reverse=True)
print(marks)


#  list.reverse # this is use to write the list inn reverse direction 
marks.reverse() #marks.reverse()
print(marks)



# list.insert( idx, el ) #insert element at index
marks.insert(66,555)
print(marks)


# list.remove(1) #removes first occurrence of element
marks.remove(1)
print(marks)

# list.pop( idx ) #removes element at idx
marks.pop(1) # it will remove element from its place no like 0,1,2,3,4
print(marks)


## adiition of  lists 
positive_no = [1, 2, 3, 4, 5, 6]
zero =[0]
negative_no = [-1, -2, -3, -4, -5, -6,]
negative_no.sort(reverse=False)# here i use sorting cause i write no in accending order but i waant them in ddesending order.
print(negative_no)
integers = negative_no + zero + positive_no
print(integers)
