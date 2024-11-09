
###Examples
# 1)Declare an empty list
empty_list = list()
print(empty_list)

#2)Declare a list with more than 5 items
fruits=["mango", "apple","lemon","banana","grapes"]
print(fruits)

#3) Find the length of your list
print(len(fruits))

# 4)Get the first item, the middle item and the last item of the list
first_fruit =fruits[0]
middle_fruit = fruits[len(fruits)//2]
last_fruit =fruits[4]
new_fruits = (first_fruit, middle_fruit, last_fruit )
print(new_fruits)



### Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types =["rutik", 22, 185.00, "unmarried", "pune"]
print(("yourinformation :"),mixed_data_types)


# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
first =it_companies[0]
second = it_companies[len(first)//2]
last = it_companies [-1]
print(first, second, last)

# Print the list after modifying one of the companies
it_companies[5]="Tcs"
print(it_companies)

# Add an IT company to it_companies
it_companies.append("Accenture")
print(it_companies)

# Insert an IT company in the middle of the companies list
middlenew =len(it_companies)//2
it_companies.insert(middlenew,"coder")
print(it_companies)
