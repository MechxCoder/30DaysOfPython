##Conditional  Statement (if - else - elif)

# #syntax(if)
# if (condition):
#     this part of code runs for truthy conditions

# Example:
a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number

## syntax (if_else)
# if (condition):
#     this part of code runs for truthy conditions
# else:
#      this part of code runs for false conditions

# Example:
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

# # syntax (if_elif_else)
# if condition:
#     code
# elif condition:
#     code
# else:
#     code

# Example:
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')


#sort hand
# syntax
# (code) if (condition) else (code)

# Example:
a = 3
print('A is positive') if a > 0 else print('A is negative') # first condition met, 'A is positive' will be printed

# Nested Conditions Conditions can be nested

# # syntax
# if (condition):
#     code/print
#     if condition:
#     code


# Example:
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')


# We can avoid writing nested condition by using logical operator and.  (If Condition and Logical Operators)
# # syntax
# if condition and condition:
#     code


# Example:
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')
    
# If and Or Logical Operators
# # syntax
# if condition or condition:
#     code

# Example:
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')






###Exammples:

#1) WAP to check if a number entered by the user is odd or even.
num=int(input("Enter the no :"))
rem=num %2
if(rem==0):
    print("The no is Even")
else:
    print("The no is odd")


#2) WAP to find the greatest of 3 numbers entered by the user.
a=int(input("Enter the 1st no :"))
b=int(input("Enter the 2nd no :"))
c=int(input("Enter the 3rd no :"))

if(a >= b and a >= c):
    print("the first no is greater")
elif(b >= c):
    print("the second no is greatest")
else:
    print("the third no is greatest")


# 3)Grade Assigner: Write a program that takes a score between 0 and 100 as input and prints the corresponding grade based on the following conditions:
# 90 and above: Grade A
# 80-89: Grade B
# 70-79: Grade C
# 60-69: Grade D
# Below 60: Grade F
score=int(input("Enter your marks :"))

if score>=90:
    print("Grade A")
elif score>=80:
    print("Grade B")
elif score>=70:
    print("Grade C")   
elif score>=60:
    print("Grade D")
else :
    print("Grade F")


# 4)Password Validation: Write a program that takes a password as input and checks if it meets the following criteria:
# At least 6 characters long.
# Contains no spaces.
# Contains at least one uppercase letter. If it meets all criteria, 
# print "Valid Password", else print "Invalid Password".
password = input("password :")
if len(password) >=6 and " " not in password and any(char.isupper()for char in password):
    print("Valid password")
else:
    print("Invalid password")



'''5) String Comparison: Write a program that takes two strings and compares them.
Print "Strings are identical" if they are the same, "Case Difference Only" if they differ only in case, and "Strings are different"
if they are completely different.'''
str1 = input("Enter the first sentence: ")
str2 = input("Enter the second sentence: ")

if str1 == str2:
    print("Strings are identical")
elif str1.lower() == str2.lower():
    print("Strings are identical\nCase Difference Only")
else:
    print("Strings are different")


#6) Check for Substring: Write a program that checks if the word "Python" is present in a given string (ignore case). If it is, print "Found"; otherwise, print "Not Found"

text = "hey i am learning a python language"

if "python" in text.lower():
    print("Found")
else:
    print("Not Found")


#7) Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
age = int(input("Enter your age:"))

if age >= 18:
    print("You are old enough to drive.")
else:
    year_remains =18-age
    print("wair for more", year_remains ,"years to drive")

# 8)Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. 
# March, April or May, the season is Spring June, July or August, the season is Summer

season = str(input("Enter the month: "))

if season in ["September","October","November"]:
    print("The current season is a Autumn")
elif season in["December", "January", "February"]:
    print("The current season is a Winter")
elif season in["march", "April", "May"]:
    print("The current season is a Spring")
elif season in["june", "july", "August"]:
    print("The current season is a Spring")
else:
    print("Invalid Month, please enter the correct month")