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