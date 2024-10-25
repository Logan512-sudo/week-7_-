
#Comparison operators
# Logical operators
# Decision making
# loops(for loops, while loops, range, enumerator)
# min/max practice
# Random in python
# List comprehension


# review practice
# Append the value of current to the end of the list seconds Please use the list.append() method to do that.


#seconds = [1.23, 1.45, 1.02]
#current = 1.11
#print(seconds.append(current))
#print(seconds)
# Remove item 1.45 from seconds.
#seconds = [1.23, 1.45, 1.02, 1.11]
#seconds.remove(1.45)
#print(seconds)

# Remove items 1.45, 1.02, and 1.11 from seconds.
#seconds = [1.23, 1.45, 1.02, 1.11]
#seconds.remove(1.45)
#seconds.remove(1.02)
#seconds.remove(1.11)
#print(seconds)

################################comparison operators#########################
#remember....
# > greater
# < less
# >= greater or equal
# <= less or equal
# == equal
# != different or not equal to




# Comparison Operators Practice  1:
# Create two variables (num1 and num2) with the following values: 36 and 17. Check if num1 is greater than or equal to num2 and store the result of that comparison in a variable called my_bool
#num1 = 36
#num2 = 17
#my_bool = (num1 >= num2)
#print(my_bool)

# Comparison Operators Practice  2:
# Create two variables (num1 and num2):
# Inside num1, store the result of the square root of 25
# Inside num2, store the number 5.
# Check if num1 is equal to num2 and store the result of that comparison in a variable called my_bool.
#from math import *
#num3 = sqrt(25)
#num4 = 5
#my_bool = (num3 == num4)
#print(my_bool)

# Comparison Operators Practice #3:
# Create two variables (num1 and num2):

# Inside num1, store the result of 64 x 3

# Inside num2, store the result of 24 x 8

# Check if num1 is different from num2 and store the result of that comparison in a variable called my_bool.
#a = 64
#b = 3
#c = 24
#d = 8
#num1 = (a*b) 
#num2 = (c*d)
#my_bool = (num1 != num2 )
#print(my_bool)


#######################comparison operators challenge#####################
# Challenge: Compare two numbers entered by the user and check if they are equal or not.
# If they are not equal, print which one is greater.

# Prompt the user for two numbers

# Check for equality and greater number

num3 = input("Type in a random number: ")
num4 = input("Type in another random number: ")
my_bool2 = (num3 == num4)
if my_bool2 is True:
    print("These numbers are equal")
else:
    print("These numbers are not equal")
my_bool2 = (num3 >= num4)
if my_bool2 is True:
    print(num3 + " is the greater number")
else:
    print(num4 + " is the greater number")
   