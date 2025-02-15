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

print_verse()

#Repetition