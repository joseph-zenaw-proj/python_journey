#Chapter 3: Functions

# Defining new functions
# A function definition specifies the name of a new function and the sequence of statements that run when the function is called. 
def print_name():
    name = "Yoseph"
    print (name)

print_name()

#Parameters
def print_age_twice(int):
    print (int)
    print (int)

print_age_twice("Yoseph")

#You can use a variable as an argument
def print_age():
    age = 3
    print (age)

print_age()

#Calling Functions
#Spam, Spam, Spam, Spam,
#Spam, Spam, Spam, Spam,
#Spam, Spam,
#(Lovely Spam, Wonderful Spam!)
#Spam, Spam,
def repeat(word, n):
    print (word * n)

spam = 'spam, '

def first_two_lines():
    repeat(spam, 4)
    repeat(spam, 4)


def last_three_lines():
    repeat(spam, 2)
    print ("(Lovely Spam, Wonderful Spam!)")
    repeat(spam, 2)


def print_verse():
    first_two_lines()
    last_three_lines()


#Repetition


def print_n_verses(n):
    for i in range(n):
        print_verse()
        print()

n = 3
print_n_verses(n)

#Variables and parameters are local
def print_twice(text):
    print(text)
    print(text)

def new_func(m, n):
    add = m + n
    print_twice(add)

new_func(5, 4)

#Parameters of the Python print function
print('the user name is joseph','zenaw' , sep="_" )

#Tracebacks
#A traceback in Python is an error report that shows where an exception occurred in your code.

#Exercise 
#Write a function named print_right that takes a string named text as a parameter and prints the string with enough leading spaces that the last letter of the string is in the 40th column of the display
def print_right(text):
    spaces = 40 - len(text)
    print(" " * spaces + text)

print_right('Hello')

#Write a function called triangle that takes a string and an integer and draws a pyramid with the given height, made up using copies of the string.

def triangle(string , height):
     for i in range(1, height + 1):
        print(string * i)

triangle("O" , 5)
print()
#Write a function called rectangle that takes a string and two integers and draws a rectangle with the given height and width, made up using copies of the string.
def rectangle(string , w , h):
    for i in range(1,  h + 1):
        print(string * w)
    
rectangle("O" , 4 , 5)
print()
# The song “99 Bottles of Beer” starts with this verse:
# 99 bottles of beer on the wall
# 99 bottles of beer
# Take one down, pass it around
# 98 bottles of beer on the wall

# Then the second verse is the same, except that it starts with 98 bottles and
# ends with 97. The song continues—for a very long time—until there are 0
# bottles of beer.
# Write a function called bottle_verse that takes a number as a
# parameter and displays the verse that starts with the given number of
# # bottles.

def bottle_verse(n):
    for i in range(n, 0, -1):  # Loop from n down to 1
        print(f"{i} bottle{'s' if i > 1 else ''} of beer on the wall")
        print(f"{i} bottle{'s' if i > 1 else ''} of beer")
        print("Take one down, pass it around")
        print(f"{i-1} bottle{'s' if i-1 != 1 else ''} of beer on the wall\n")

    print("No more bottles of beer on the wall!")  

bottle_verse(4)  


# Write a function called countdown_song that takes a number and prints a countdown song like this:

# 5 days left until the event
# 4 days left until the event
# 3 days left until the event
# 2 days left until the event
# 1 day left until the event
# No more days left!
print()
def countdown_song(n):
    for i in range(n , 0 , -1):
        print(f"{i} day{'s' if i > 1 else ''} left until the event")

    print("No more days left!")

countdown_song(3)
print()
#Write a function reverse_count(n) that prints numbers from n down to 1, then prints "Blastoff!"
def reverse_count(n):
    for i in range(n, 0 , -1):
        print(i)
    
    print("Blastoff!")

reverse_count(5)
print()

#Write a function print_table(n) that prints the multiplication table for n from 1 to 10
def print_table(n):
    for i in range(1 , 11):
        print(f"{n} x {i} = {n * i}")

print_table(4)
print()

#Write a function word_pyramid(word, height) that prints a pyramid using the given word
def word_pyramid(word, height):
    for i in range(1, height + 1):
        print(word * i)

word_pyramid("D", 6)
