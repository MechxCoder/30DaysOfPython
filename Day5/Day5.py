# Practice questions on if else elif conditional statement and on strings


# Grade Assigner: Write a program that takes a score between 0 and 100 as input and prints the corresponding grade based on the following conditions:
# 90 and above Grade A
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



# Password Validation: Write a program that takes a password as input and checks if it meets the following criteria:

# At least 6 characters long.
# Contains no spaces.
# Contains at least one uppercase letter. If it meets all criteria, 
# print "Valid Password", else print "Invalid Password".


password = input("password :")
if len(password) >=6 and " " not in password and any(char.isupper()for char in password):
    print("Valid password")
else:
    print("Invalid password")



# String Comparison: Write a program that takes two strings and compares them.
#  Print "Strings are identical" if they are the same, "Case Difference Only" if they differ only in case, and "Strings are different"
#  if they are completely different.


str1 = input("Enter the first sentence: ")
str2 = input("Enter the second sentence: ")

if str1 == str2:
    print("Strings are identical")
elif str1.lower() == str2.lower():
    print("Strings are identical\nCase Difference Only")
else:
    print("Strings are different")


# Check for Substring: Write a program that checks if the word "Python" is present in a given string (ignore case).
#  If it is, print "Found"; otherwise, print "Not Found"


# str.count("am")
text = "hey i am learning a python language"

if "python" is in the text.lower():
    print("Found")
else:
    print("Not Found")
