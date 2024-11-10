### Operators
''' Arithmetic Operators:
Addition(+): a + b
Subtraction(-): a - b
Multiplication(*): a * b
Division(/): a / b
Modulus(%): a % b
Floor division(//): a // b    
Exponentiation(**): a ** b   '''

# Ex:
print("Addition:", 1+2)
print("substaction:", 6-5)
print("Multiplication:", 4*5)
print("Division",20/5)
print("modulus:", 20%5)          #remainder
print("Floor division",50//5)     
print("Exponentiation", 2**5)    #2raise to 5

# Floating numbers
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))

# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         # Adding unit to the weight

# Calculate the density of a liquid
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3

##Comparison Operators
print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Comparing something gives either a True or False
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)




###Exercises - Day 3
#1)Declare your age as integer variable
my_age=22
print(type(my_age))
print(my_age)

#2)Declare your height as a float variable
my_height=179.99
print(type(my_height))
print(my_height)

#3)Declare a variable that store a complex number
comp_vari= 1+2j
print(type(comp_vari))
print(comp_vari)

#4) Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle
base=int(input("Enter the base:"))
height=int(input("Enter the height:"))
print(0.5*base*height)

#5) Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
sidea=int(input("Enter the sideA:"))
sideb=int(input("Enter the sideB:"))
sidec=int(input("Enter the sideC:"))
print(sidea+sideb+sidec)


#6)Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
age = float(input("Enter the no of year you lived:"))
print(age*3.154e+7)

#7)Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
area_of_circle = float(input("enter the are of circle:"))
pi =float(3.14)
print(pi*area_of_circle*area_of_circle)