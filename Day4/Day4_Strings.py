#Strings ( it is an datatype and it stores and diff type of character)
# there are 3 ways to write the strinngs 
str1= "this is the first type to write the string"
str2= 'this is the 2nd type of writing string'
str3= '''this is the 3rd type of writing string'''
print(str1)
print(str2)
print(str3)

# all this types are valid for writing the string this types used because sometimes we need to use the apastropy, if you use the apastopy the  the strings not valid Ex:
str = "I don't want to go there "    # if we start string with the single quote then the string will ennd at the 'don' then the next sentences will not be valid in the str
print(str)

#multiline str
multiline_string = '''I am a student and enjoy studying.
I didn't find anything as rewarding as upskalling yourself.
That is why I started python learning.'''
print(multiline_string)

# Another way of doing the same thing
multiline_string = """I am a student and enjoy studying.
I didn't find anything as rewarding as upskalling yourself.
That is why I started python learning."""
print(multiline_string)

# String concatination ( it is use to add 1str into other str ) Ex:
str1 = "hello" " "   # here i use empty " " for ging the space in str 
str2 = "world"
str=(str1+" "+str2)   # this  also valid 
print(str)

'''Escape sequance characters
\n: new line
\t: Tab means(4 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (") '''

'''python Strings as Sequences of Characters
Python strings are sequences of characters, and share their basic methods of access with other Python ordered sequences of objects – lists and tuples. The simplest way of extracting single characters from strings (and individual members from any sequence) is to unpack them into corresponding variables.
'''
# Unpacking Characters
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

# Lenght of str (this is used to find out the lenght of str)
str = "hello rutik"  # in python the empty space also count in the str
lenght = len(str)
print(lenght)
      #or
print(len(str))  #this will  also print the lenght of the str

# Indexing ( it is helpfull to acess the characters in  the python):
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

str = "this is the world of coders, here the people  learn and earn th coding skills "
# in pyhton the counting of the string will start from 0 like 0123 then goes on
print(str[0:11]) #(this is the) output but here when you write the last strinng no this will not gone print in the output Ex:

str = "hello" 
print(str[0])  #h

# String slicing ( ist is nothing but the negative inndexing it is used for accesing the str dromm the end )
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

str ="rutik"
print(str[-3:-1])

# We can easily reverse strings in python.

greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH

# Skipping Characters While Slicing It is possible to skip characters while slicing by passing step argument to slice method.

language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto

#String Functions (this is some fuction that we use it the string)
str ="i am a mechanical enginneer" 
# 1)str.endsWith("er.") returns true if string ends with substr
print(str.endswith("er")) #True

# 2)str.count("am") #counts the occurrence of substr in string
print(str.count("am")) #1

# 3)str.capitalize( ) #capitalizes 1st char
print(str.capitalize()) #I am a mechanical enginneer

#4)str.replace("am","is" ) #replaces all occurrences of old with new
print(str.replace("am","is")) #i is a mechanical enginneer

# str.find( "word" ) #returns 1st index of 1st occurrence
print(str.find("mechanical")) #7

# startswith(): Checks if String Starts with the Specified String
print(str.startswith('i')) # True


# Exercises - Day 4
#1) WAP to input user’s first name & print its length.
str= input(" Enter your name :")
str=(len(str))
print(str)


#2) WAP to find the occurrence of ‘$’ in a String.
str="hheyy i am $ and the the current exchange of $ to Rs 1$ is equal to 83.55"
print(str.count("$"))

#3)Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'
str1= "Thirty"
str2= "days"
str3= "of"
str4= "pyhton"
print(str1, str2, str3, str4)

# 4)Declare a variable named company and assign it to an initial value "Coding For All".
company  ="coding For All"

#5)Print the variable company using print().
print(company)

#6)Print the length of the company string using len() method and print().
print(len(company))

#7)Change all the characters to uppercase letters using upper() method.
print(company.upper())

#8)Change all the characters to lowercase letters using lower() method.
print(company.lower())
