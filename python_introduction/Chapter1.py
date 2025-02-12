import math
#Chapter 1: Programming as a way of thinking
#Arithmetic Operators and Expressions
print (3 + 6 * 2)
print ((3 + 6) * 2)
print (3^2) #Bitwise operator
#Arithemtic Functions: Parentheses is required while calling a function
print( round(2.8/2))
print( abs(-99))
#Strings
print ('Hello There')
print ("It's me")
print ("Joseph " + "Zenaw") 
print ("I am happy " * 3)
#Built in function: len
print (len("joseph"))
#Values and Types
print (type("a string"))
print (type(23))
print (type(23.5))
print (float(23))
print ((int("123")) + 77)
print (int(float("123.4")))
print (1,000,000)
#Formal and Natural Languages
#Natural languages are the languages people speak, like English, Spanish,
#and French. They were not designed by people; they evolved naturally.
#Formal languages are languages that are designed by people for specific applications.

#Debugging
print (round(123.23 , -1))
print (round(math.pi, -1))
print (abs(-7.0))
#Exercise
#How many  seconds are there in 42 minutes and 42 seconds
totSeconds = (42 * 60) + 42 
print ("There are " + str(totSeconds) + " seconds in 42 minutes and 42 seconds")
#How many miles are there in 10 kilometers?
totMiles = round((10 / 1.61) , 2)
print ("There are " + str(totMiles) + " miles in 10 kilometers")
#If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace in seconds per mile?
avgPace = totSeconds / totMiles
print ("The average pace in seconds per mile is " + str(avgPace))
#What is your average pace in minutes and seconds per mile?
avgPaceMin = (totSeconds / 60) / totMiles
print ("The average pace in minutes and seconds per mile is " + str(avgPaceMin))
#What is your average speed in miles per hour
avgPaceHour = (totMiles / (totSeconds / 3600))
print ("The average speed in miles per hour is " + str(avgPaceHour))