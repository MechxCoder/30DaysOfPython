# Variables 

# In python variables is a container that stores a information about 
# variable is like creating a placeholder in memory and assigning a some value to it 

first_name = 'Rutik'
last_name = 'Barde'
country = 'India'
city = 'Pune'
age = 22
is_married = False
skills = ['currently learning Python'] # you can use (" ") or (' ') for the variable but only if  it is a character otherwise we dont need to use this 


print('First name:', first_name)
print('First name length:', len(first_name)) # "I use len to find out how many characters are contained in my name."
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)  


'''
rules for identifiers (Identifiers = the name or any type of word except keywords )
1) Identifiers can be combination of uppercase and lowercase,digits and undercase but we cannot use @ %* in the variable 
2) An identifier can not start with the digit 
3) we cannot use special symbols in the variabbles (@#*!$)
4) Identifier  can be any lenght '''




# Datatypes 
''' 
In python there are 5 main datatypes 
1) Integers : Integer could be +ve, -ve, or 0  ex: 29, -30, 0 
2)String    : Sring means we can store any name, word or sentence in it but,
                    when we use str datatype we have to use ("rutik") or ('rutik') means use collean 
3) Float    : when we have to use decimal values then we use the float datatype  ex: 29.99, 30.88 
4) Boolean  : It carries true or false value but when you write True and False initials in lowercase its not valid in variables
5) None     : It carries None value '''


# Keywords  This cannot be the name of variables because this  keywords use in python for other operation 
'''
And      else      in           return        as       expect      is      True       Assert     finally    lambda 
try      break     false        nonlocal      with     class       for     import     raise      if         elif
none     while     continue     from          not      field       def     global     or         del        pass   
'''

# Que : write a program for sum of two variavles 
a =10
b =25
sum = (a + b )
print (sum)



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


a = int("5")
b = 23

print (type(a))
print ( a + b) # here we convert str to int this will not give you error 


# Get input from the user
Name = input("Enter your name: ")  # Get input from user

# Print a greeting message
print("Hello", Name, "what are you doing?")



#Write a program that asks for the user's name, age, and favorite color, and then prints a sentence using all three inputs.
Name = input ("Enter your name ")
Age = input ("Enter your age ")
Favoritecolor = input ("Enter your favorite color ")

print ("Hello", Name,"," "Your age is", Age,"," "and your favorite color is", Favoritecolor )
