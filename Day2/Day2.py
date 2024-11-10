## Variables 
# In python variables is a container that stores a information about variable is like creating a placeholder in memory and assigning a some value to it 

#Creating varibles:
first_name = 'Rutik'
last_name = 'Barde'
country = 'India'
city = 'Pune'
age = 22
is_married = False
skills = ['currently learning Python'] # you can use (" ") or (' ') for the variable but only if  it is a character otherwise we dont need to use this 

#printing variables :
print('First name:', first_name)
print('First name length:', len(first_name)) # "I use len to find out how many characters are contained in my name."
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)  


'''Identifiers:
rules for identifiers (Identifiers = the name or any type of word except keywords )
1) Identifiers can be combination of uppercase and lowercase,digits and undercase but we cannot use @ %* in the variable 
2) An identifier can not start with the digit 
3) we cannot use special symbols in the variabbles (@#*!$)
4) Identifier  can be any lenght

Invalid variables names:
first-name
first@name
first$name
num-1
1num   '''


## Datatypes 
''' 
In python there are 5 main datatypes 
1) Integers : Integer could be +ve, -ve, or 0  ex: 29, -30, 0 
2)String    : Sring means we can store any name, word or sentence in it but,
            when we use str datatype we have to use ("rutik") or ('rutik')  use collean 
3) Float    : when we have to use decimal values then we use the float datatype  ex: 29.99, 30.88 
4) Boolean  : It carries true or false value but when you write True and False initials in lowercase its not valid in variables
5) None     : It carries None value '''

# Keywords (Built inn functions that cannot use as a varibles name ) This cannot be the name of variables because this  keywords use in python for other operation 
'''
And      else      in           return        as       expect      is      True       Assert     finally    lambda 
try      break     false        nonlocal      with     class       for     import     raise      if         elif
none     while     continue     from          not      field       def     global     or         del        pass   
'''

# Type conversion 
''' 
Assume i have a variable and the type of that variabe is int and i want to change the type of
 variable into float it is called type conversion 
'''
a = 1
b = 3.5
sum =(a + b)
print (sum ) # this will not  give you error because pythonn interpriter  automatically converts int into float because 
# float have the suppperier value than int 

# type  casting here we forcefully convert datatype one to other 
#  But when you try to add str to any oother datatype it will give you error Ex: 

# a = "55"
# b = 23
# sum =(a + b)
# print (sum) # can only concatenate str (not "int") to str you will face this error instead you convert your str to int 

# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
num_float = float(num_str)
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10

# str to list
first_name = 'Rutik'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['R', 'u', 't', 'i', 'k']



# #Get input from the user
Name = input("Enter your name: ")  # Get input from user
# Print a greeting message
print("Hello", Name, "what are you doing?")

#Write a program that asks for the user's name, age, and favorite color, and then prints a sentence using all three inputs.
Name = input ("Enter your name ")
Age = input ("Enter your age ")
Favoritecolor = input ("Enter your favorite color ")

print ("Hello", Name,"," "Your age is", Age,"," "and your favorite color is", Favoritecolor )


# #Que :
# 1) write a program for sum of two variavles 
a =10
b =25
sum = (a + b )
print (sum)



### solving and practicing :-###

''' 1. Variables Practice
Define two variables, a and b, and assign them values 5 and 10. 
Then, swap the values of a and b without using a third variable. 
Print the values of a and b after swapping.
AnSWER'''

a = 55
b = 66
a,b=b,a
print (a,b)


'''2. Data Types
Create a variable for each basic data type (integer, float, string, and boolean).
 Print each variable and use the type() function to display its data type.
ANSWER'''

a = 55
b = 66.59
c = "rutik"
d = True

print (type(a))
print (type(b))
print (type(c))
print (type(d))


'''3. Simple Arithmetic
Write a Python program to ask the user for two numbers and then calculate and display
their sum, difference, product, and division.
ANSWER'''

num1  = int(input("Enter your first no:"))
num2  = int(input("Enter your second no:"))

sum        = (num1+num2)
difference = (num1-num2)
product    = (num1*num2)
division   = (num1/num2)

print (sum)
print (difference)
print (product)
print (division)



'''4. Type Conversion
Take an input from the user (string) and convert it to an integer, 
then multiply it by 10 and print the result.(Handle cases where the input may not be convertible to an integer.)
ANSWER'''

a = input("Enter your number:")

a= int(a)
ans= (a*10)
print("Result:", ans)


'''5. String Manipulation
Create a string variable with your name. Then print:
The first character of your name.
The last character of your name.
The length of your name using len().
ANSWER'''


name = input("Enter your name:")
 
print ("The First character of your name:", name[0])
print ("The Last character of your name:", name[-1])
print ("The length of your name:", len(name))



'''6. Concatenation
Take two inputs from the user (both as strings) and concatenate them to form a single string. Print the result.
ANSWER'''

string1 =input("Enter the first string:")
string2 =input("Enter the second string:")
string=(string1+string2)
print("your concatinated string is:", string)


'''7. User Input and Arithmetic
Ask the user to input a number and then print the square of that number. Make sure to handle any type conversion necessary.
ANSWER'''

num1 = int(input("Enter your no:"))
square=(num1*num1)
print(square)