# Solving and practicing Questions on Variables, Datatypes, and input from the user:-

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

