# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

# Creating a Dictionary: To create a dictionary we use curly brackets, {} or the dict() built-in function.
empty_dict = {}
print(empty_dict)

info_student ={
    "name" :"Rutik",
    "sub" :("tm", "hvac", "dom",),
    "age" : 22,
    "country" : "india",
    "married_status":"True"
}
print(info_student)
print(len(info_student))

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person)

# Modifying Items in a Dictionary: We can modify items in a dictionary
# # syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'
print(dct)
print(len(dct))

# Checking Keys in a Dictionary: We use the in operator to check if a key exist in a dictionary
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False

# Removing Key and Value Pairs from a Dictionary
# 1)pop(key): removes the item with the specified key name:
dct.pop('key1')
print(dct)
# 2)popitem(): removes the last item
dct.popitem()
# 3)del: removes an item with specified key name
del dct['key2']

# Changing Dictionary to a List of Items: The items() method changes dictionary to a list of tuples.
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items())

# Clearing a Dictionary:If we don't want the items in a dictionary we can clear them using clear() method
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None

# Deleting a Dictionary: If we do not use the dictionary we can delete it completely
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct

# Copy a Dictionary: We can copy a dictionary using a copy() method. Using copy we can avoid mutation of the original dictionary.
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

# Getting Dictionary Keys as a List: The keys() method gives us all the keys of a a dictionary as a list.
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])

# Getting Dictionary Values as a List: The values method gives us all the values of a a dictionary as a list.
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])


###Exercise:
# 1)Create an empty dictionary called dog
empty_dog ={}

# 2)Add name, color, breed,  age to the dog dictionary
dog = {
    'name': 'bruno',
    'color': 'brownish',
    'breed':'german shefard',
    'age':10
}
print(dog)

# 3)Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student_dct ={
    'first_name':'rutik', 
    'last_name':'Barde',
    'gender':'Male', 
    'age':22, 
    'marital status':'unmarried', 
    'skills':['python'], 
    'country':'India', 
    'city':'pune' ,
    'address':{
        'street':'Space street',
        'zipcode':'412028'
    }
}
print(student_dct)

# 4)Get the length of the student dictionary
print(len(student_dct))

# 5)Get the value of skills and check the data type, it should be a list
skills = student_dct['skills']
print('skills:', skills)

# 6)Modify the skills values by adding one or two skills
student_dct['skills'].extend(['python','programer'])
print(student_dct)

# 7) Get the dictionary keys as a list
dct_keys = list(student_dct.keys())
print("Dictionary keys:", dct_keys)

# 8)Get the dictionary values as a list
print(list(student_dct))

# 9)Change the dictionary to a list of tuples using items() method
list_of_tuple= list(student_dct.items())
print(list_of_tuple)