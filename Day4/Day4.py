#Strings ( it is an datatype and it stores and diff type of character)
# there are 3 ways to write the strinngs 
str1= "this is the first type to write the string"
str2= 'this is the 2nd type of writing string'
str3= '''this is the 3rd type of writing string'''
print(str3)



# all this types are valid for writing the string this types used because sometimes we need to use the apastropy if you use the apastopy 
# the  the strings not valid Ex:
str = "I don't want to go there "    # if we start string with the single quote then the string will ennd at the 'don' then the next sentences will not be valid in the str
print(str)



# String concatination ( it is use to add 1str into other str ) Ex:
str1 = "hello" " "   # here i use empty " " for ging the space in str 
str2 = "world"
str=(str1+" "+str2)   # this  also valid 
print(str)



# Lenght of str (this is used to find out the lenght of str)
str = "hello rutik"  # in python the empty space also count in the str
lenght = len(str)
print(lenght)



# Indexing ( it is helpfull to acess the characters in  the python) Ex:
str = "this is the world of coders, here the people  learn and earn th coding skills "
# in pyhton the counting of the string will start from 0 like 0123thenn goes on
print(str[0:11]) #this is the  this  is the outputbut here when you write the last strinng no this will not gonne print in the output Ex:
str = "hello" 
print(str[0:4]) #here the"hel" this output you will get
print (str[:3]) # the python interpritor will start string count from the start if you not mention the starting no and same with end no
print(str[3:])



# String slicing ( ist is nothing but the negative inndexing it is used for accesing the str dromm the end )
str ="rutik"
print(str[-3:-1])



#String Functions (this is some fuction that we use it the string)
# str ="I am a mechanical enginneer." 
# str.endsWith("er.") #returns true if string ends with substr

# str.count("am") #counts the occurrence of substr in string
# str.capitalize( ) #capitalizes 1st char
# print(str.replace("am","is" )) #replaces all occurrences of old with new

# str.find( word ) #returns 1st index of 1st occurrence



#QUESTION : WAP to input user’s first name & print its length.
str= input(" Enter your name :")
str=(len(str))
print(str)



# QUESTION : WAP to find the occurrence of ‘$’ in a String.
str="hheyy i am $ and the the current exchange of $ to Rs 1$ is equal to 83.55"
print(str.count("$"))



##Conditional  Statement (if - else - elif)
# WAP to check if a number entered by the user is odd or even.

num=int(input("Enter the no :"))


rem=num %2
if(rem==0):
    print("The no is Even")
else:
    print("The no is odd")



# WAP to find the greatest of 3 numbers entered by the user.
a=int(input("Enter the 1st no :"))
b=int(input("Enter the 2nd no :"))
c=int(input("Enter the 3rd no :"))

if(a >= b and a >= c):
    print("the first no is greater")
elif(b >= c):
    print("the second no is greatest")
else:
    print("the third no is greatest")
