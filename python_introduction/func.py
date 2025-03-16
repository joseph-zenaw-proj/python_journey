def greet(name):
    print("Hellow, " + name)

greet("Yoseph")

def is_even(n):
    return n % 2 == 0

print(is_even(4))

def is_odd(n):
    return (n+1) % 2 == 0

print(is_odd(1))

def reverse_string(s):
    return s[::-1]

print(reverse_string("ABC"))

def add(n, m):
    return n + m

print(add(3, 6))

#check how it works
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

print(sum_of_digits(123))

def reverse_string(s):
    return s[::-1]

print(reverse_string('fool'))

#check how it works
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

print(count_vowels('the quick brown fox jumps over the lazy dog'))

def check_reverse(s, t):
    return s == t[::-1]

print(check_reverse('racecar', 'raceca'))
#check how it works
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(2))

def multiply(n, m):
    return n * m

print(multiply(2, 3))

def divide(n, m):
    return n / m

print(int(divide(4, 2)))

def divmult(n, m, o):
    return n / m * o

print(divmult(1, 2, 3))


def multdiv(n, m, o):
    return n * m / o

print(divmult(1, 2, 3))

def addsub(n, m, o):
    return n + m - o

print(addsub(8, 9, 10))


def subdiv(n, m, o):
    return n - m / o

print(subdiv(5, 7, 9))

def trueorfalse(n, m):
    return n == m

print(trueorfalse(8, 8))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(4))    

def greet(name):
    print("Hello, " + name)

greet("Joseph")

def is_palindrome(a):
    if a == a[::-1]:
        return ("The string is a palindrome")
    return ("The string is not a palindrome")

print(is_palindrome("aabba"))

def check_equal(a, b):
    if a == b[::-1]:
        return ("They are reverse of each other")
    return ("They are not reverse of each other")

print(check_equal("foul", "luof"))

def apply_twice(func, x):
    return func(func(x))

def add_one(n):
    return n + 1

print(apply_twice(add_one, 5))