#Chapter 2: Variables and Statements
#Variables
name = " Joseph"
message = "hello there"
age = 23
print (message + name + " after one year you will be " + str(age)+ " years old.")
print (len(str(age)))
#Variable names
#numbers,letters and underscore
valid_variable_name = "good variable name"
#The import statement
#The following statement imports the math module
#A module is a collection of variables and functions.
import math

print (round(math.sqrt(100)))
print (round(math.pow(6 , 2)))
#Expressions and Statements
#Expressions
print (20 + age + round(math.pi) * 2)
#Computing the value of an expression is called evaluation
#A statement is a unit of code that has an effect, but no value.
var_name = 12 #This is a statement, it has an effect but the statement itself has no value
#Running a statement is called execution.

print ("The value of pi is :" , math.pi)
#Arguments
#When you call a function, the expression in parenthesis is called an argument.

#A function that takes one argument
print (int('123'))
#A function that takes two
print (math.pow(4 , 2))
#The function int can take a second argument that specifies the base of the number
print (int('1010' , 2)) # changes 1010 from base 2 (binary) into int which is base 10
#Another function that can take a second argument is round
#In round function the second argument is the number of decimal places to round off to
print (round(math.pi , 3))
#Functions like print can take any number of arguments

#If you call a function and provide too many arguments, that’s a typeerror
# print (float('123' , 2)) this shows 

#Exercise
#What is the volume of a sphere with radius 5?
radius = 5
volume_sphere = 4/3 * ((math.pi) * (math.pow(radius , 3)))

print ("The volume of a sphere with radius " + str(radius) + " is " + str(round(volume_sphere , 2)))

#A rule of trigonometry says that for any value of x, (cos x)**2 + (sin x)**2 = 1. Let’s see if it’s true for a specific value of x like 42.
x = 42
print ((math.cos(x)**2 + math.sin(x)**2))

#let’s compute e**2 three ways:

print (math.e**2)
print (math.pow (math.e , 2))
print (math.exp(2))