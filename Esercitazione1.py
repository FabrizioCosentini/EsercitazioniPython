# Task on input and print commands
# Verb1=input("Write a verb: ")
# print("I can", Verb1, "better than you!")
# print (4*(Verb1+" ")+Verb1)
#
# Task on Newton's Method (on print and input)
# x=int(input("What x to find the cube root of? "))
# g=int(input("What guess to start with? "))
# print("Current estimate cubed = ", g**3)
# next_g=g-((g**3-x)/(3*g**2))
# print("Next guess to try = ", next_g)
#
# f-strings task
# num=3000
# fraction=1/3
# print(num*fraction, "is", fraction*100, "% of", num)
# print(num*fraction, "is", str(fraction*100) + "% of", num)
# print(f"{num*fraction} is {fraction*100}% of {num}")
#
# Guess the number? task
# secret = 8
# guess = int(input("What is your guessed number? "))
# print(guess == secret)
#
# If number task
# x = int(input("Enter a number for x: "))
# y = int(input("Enter a different number for y: "))
# if x==y:
#    print (x, "is the same as", y)
#    print ("These are equal!")
#
# If task 2
# x=float(input("Enter a number for x: "))
# y=float(input("Enter a number for y: "))
# if x == y:
#    print ("x and y are equal")
#    if y != 0:
#        print("therefore, x/y is", x/y)
# elif x < y:
#    print ("x is smaller")
# else:
#    print ("y is smaller")
# print("thanks!")
#
# Guess too low, high, or equal task
# secret = 9
# guess = int(input("Try to guess my same number: "))
# if secret == guess:
#    print("You guessed my number!")
# elif guess < secret:
#    print("Too low!")
# else:
#    print("Too high!")
#
# Lost in the Forest task (refined)
# where = input ("You're lost in the forest. Go left or right? ")
# n_tries = 0
# while where.lower() != "left" and n_tries < 2:
#    if where.lower() == "right":
#        n_tries += 1
#        if n_tries < 2:
#            where = input("You're still lost in the forest. Go left or right? ")
#    else:
#        print("You can only go left or right.")
#        where = input ("Again, go left or right? ")
# if n_tries < 2:
#    print("You got out of the forest!")
# else:
#    print(":(")
#
# Non-integer Task
# n = int(input("Enter a non-negative integer: "))
# while n > 0:
#    print ("X")
#    n=n-1
#
# Factorial finder Task
# x = 4
# i = 1
# factorial = 1
# while i <= x:
#    factorial *=i
#    i +=1
# print(f"{x} factorial is {factorial}")
#
# Total sum Task
# mysum = 0
# start = 5
# end = 10
# for i in range (start, end+1):
#    mysum += i
# print(mysum)
#
# Break Task
# mysum = 0
# for i in range (5, 11, 2):
#    mysum += i
#    if mysum == 5:
#        break
#        mysum += 1
# print(mysum)
#
# Find number of even numbers task
# n_even = 0
# for i in range (10):
#    if i%2 ==0:
#        n_even += 1
# print(n_even)
#
# robot cheerleaders task
# an_letters="aefhilmnorsxAEFHILMNORSX"
# word = input ("I will cheer for you! Enter a word: ")
# times = int(input("Enthusiasm level from 1 to 10: "))
#
# for w in word:
#    if w in an_letters:
#        print ("Give me an " + w + ": " + w)
#    else:
#        print( "Give me a " + w + ": " + w)
# print("What does that spell?")
# for i in range (times):
#    print (word, "!!!")
#
# unique letters task
# s ="abca"
# c_seen = ""
# for c in s:
#    if c not in c_seen:
#       c_seen+=c
# print(len(c_seen))
#
# Perfect square root finder
# guess =0
# neg_flag = False
# x = int(input("Enter an integer: "))
# if x < 0:
#    neg_flag = True
# while guess**2 < x:
#    guess += 1
# if guess**2 == x:
#    print(" Square root of", x, "is", guess)
# else:
#    print(x, "is not a perfect square")
#    if neg_flag:
#        print ("just checking... Did you mean " + str(-x) + "?")
#
# Guess secret number
# secret = 5
# for guess in range(1, 11):
#    if guess == secret:
#        print("The secret number is", guess)
#        break
# if guess != secret:
#    print("The secret number wasn't found")
#
# Perfect cube finder
# q = int(input("Enter an integer: "))
# for guess in range (abs(q)+1):
#     if guess**3 >= abs(q):
#         break
# if guess**3 ==abs(q):
#         if q<0:
#             guess = -guess
#         print (" The cuber root of", q, "is", guess)
# else:
#     print(q, "is not a perfect cube")
#
# Word problems
# for A in range(1001):
#     B = A - 20
#     C = 2*A
#     if (A+B+C)==1000:
#         print("Alyssa has sold", A, "tickets")

#Binary number converter
# n = int(input("Write an integer number: "))
# bin = ""
# n_1 = n
# if n ==0:
#     bin = "0"
# if n < 0:
#     n=abs(n)
# while n > 0:
#     bin = str(n%2) + bin
#     n = n//2
# if n_1 < 0:
#     print(n_1, "is equal to -" + str(bin), "in binary notation")
# else:
#     print(n_1, "is equal to", bin, "in binary notation")

#Binary Decimals Finder
# x = input("Choose a decimal: ")
# p=0
# while ((2**p)*float(x))%1 != 0:
#     print ("Remainder = " + str((2**p)*float(x) - int((2**p)*float(x))))
#     p+=1
# num = int(float(x)*(2**p))
# result =""
# if num == 0:
#     result = "0"
# while num > 0:
#     result = str(num%2) + result
#     num = num//2
# for i in range (p-len(result)):
#     result = "0"+ result
# result = result [0:-p] + "." + result [-p::]
# print("The binary representation of the decimal " + str (x) + " is " + str(result))

#Approx task
# x = input("Choose a number: ")
# epsilon = 0.01
# n_guesses = 0
# guess = 0.0
# increment = 0.00001
# while abs(guess**2 - float(x)) >= epsilon and guess**2 <= float(x):
#     guess += increment
#     n_guesses += 1
# print(n_guesses, "guesses were taken")
# if abs (guess**2 - float(x)) >= epsilon:
#     print("An acceptable guess wasn't found.")
# else:
#     print(guess, "is close to square root of", x)

#Precise and Fast Bisection task
# x = float(input("Choose a number: "))
# epsilon = 0.0001
# n_guesses = 0
# if x < 0:
#     print("The number has no real square roots")
# else:
#     if 0 < x < 1:
#         low = x
#         high = 1.0
#     else:
#         low = 0.0
#         high = x
#     guess = (high + low)/2.0
#     while abs (guess**2 - x) >= epsilon:
#         if guess**2 < x:
#             low = guess
#         else:
#             high = guess
#         guess = (high + low)/2.0
#         n_guesses += 1
#     print(n_guesses, "guesses were taken")
#     print(guess, "is close to square root of", x)

#Bisection Cube Root Task
# x = float(input("choose a number: "))
# epsilon = 0.0001
# if x == 0:
#     print("The cubic root of 0 is equal to 0")
# else:
#     if x > 0:
#         if 0 < x < 1:
#             low = x
#             high = 1
#         else:
#             low = 0
#             high = x
#     else:
#         if -1 < x < 0:
#             low = -1
#             high = x
#         else:
#             low = x
#             high = 0
#     guess = (high + low)/2.0
#     while abs (guess**3 - x) >= epsilon:
#         if guess**3 > x:
#             high = guess
#         else:
#             low = guess
#         guess = (high + low)/2.0
#     print(guess, "is close to cubic root of", x)

# Newton-Raphson root finder
# epsilon = 0.000001
# k = float(input("Choose a number: "))
# guess = k/2.0
# n_guesses = 0
# while abs(guess**2 -k) >= epsilon:
#     n_guesses += 1
#     guess = guess - ((guess**2 - k)/(2*guess))
# print(n_guesses, "guesses were made")
# print("The square root of " + str(k) + "is about " + str(guess))

#Creating a function
# def is_even(i):
#     """ Input: i, a positive int
#     Returns True if i is even, False otherwise"""
#     return i%2 == 0
#
# print(is_even(3))
# print(is_even(8))

#Create a function #2 Task
# def div_by(n, d):
#     """n and d are ints > 0
#     Returns True if d divides n evenly and False otherwise"""
#     return n%d ==0
#
# print(div_by(10,3))
# print(div_by(195,13))

#Create sum_odd(a, b) Task
# def sum_odd(a, b):
#     """ a and b are the integer ends of a list of numbers
#     Returns the sum of the odd integers between a and b"""
#     sum_of_odds = 0
#     for i in range(a, b+1):
#         if i%2==1:
#             sum_of_odds += i
#     return sum_of_odds

#Fix the function Task
# def is_triangular(n):
#     """n is an int > 0
#     Returns True if n is triangular, i.e. equals a continued summation of natural numbers (1+2+3+...+k), False otherwise"""
#     total=0
#     for i in range(n+1):
#         total += i
#         if total ==n:
#             return True
#     return False
#
# print(is_triangular(1))

#Create bisection_root function
# def bisection_root(x):
#     epsilon =0.000001
#     low= 0
#     high = x
#     ans = (high + low)/2.0
#     while abs (ans**2-x) >= epsilon:
#         if ans**2 < x:
#             low=ans
#         else:
#             high =ans
#         ans=(high +low)/2.0
#     return ans
#
# print(bisection_root(float(input("Choose a positive integer: "))))

#Count_nums_with_sqrt_close_to Task
# def count_nums_with_sqrt_close_to(n, eps ilon):
#     """n is an int > 2
#         epsilon is a positive number < 1
#     Returns how many integers have a square root within epsilon of n"""
#     n_nums = 0
#     for i in range(n**3):
#         root = bisection_root(i)
#         if abs(n - root) < epsilon:
#             n_nums += 1
#         if root > n + epsilon:
#             break
#     return n_nums
#
# print(count_nums_with_sqrt_close_to(10, 1))

#Different Scopes task
# def f(x):
#     x = x + 1
#     print("In f(x): x =", x)
#     return x
#
# print(f(1))

#Functions as objects task
# def calc(op, a, b):
#     return op(a, b)
#
# def add(a, b):
#     return a + b
#
# def div(a, b):
#     if b !=0:
#         return a / b
#     print("Denominator was 0.")

#Functions as parameters Example
# def func_a():
#     print("inside func_a")
# def func_b(y):
#     print("inside func_b")
#     return y
# def func_c(f, z):
#     print("inside func_c")
#     return f(z)
#
# # print(func_a())
# # print(5 + func_b(2))
# print(func_c(func_b, 3))

#Functions as parameters Task
# def apply(criteria, n):
#     """* criteria is a func that takes in a number and returns a bool
#         * n is an int
#     Returns how many ints from 0 to n (inclusive) match the criteria (i.e. return True when run with criteria)"""
#     count = 0
#     for i in range(n +1):
#         if criteria(i):
#             count += 1
#     return count
#
# print(apply(is_even, 10))

#Lamba Example
# print(apply(lambda x: x%2 == 0, 10))

#Lambda Task
# def do_twice(n, fn):
#     return fn(fn(n))
#
# print(do_twice(3, lambda n: n ** 2))

#Tuple Test
# seq = (2, "a", 4, (1, 2))
#
# print(len(seq))
# print(seq[3])
# print(seq[-1])
# print(seq[3] [0])
# print(seq[4])

#Switching values with tuples
# x = 1
# y = 2
# (x, y) = (y, x)
# print(x)
# print(y)

#Return more than one value
# def quotient_and_remainder(a, b):
#     q = a // b
#     r = a % b
#     return q, r
#
# print(quotient_and_remainder(5, 2))
#
# (quot, rem) = quotient_and_remainder(5, 2)
#
# print("The quotient is", quot)
# print("The remainder is", rem)

#Char_counts task
# def char_counts(s):
#     """s is a string of lowercase chars
#     Return a tuple where the first element is the number of vowels in s and the second element is the number of consonants in s"""
#     vowels = "aeiou"
#     n_vowels = 0
#     n_consonants = 0
#     for char in s:
#         if char in vowels:
#             n_vowels += 1
#         else:
#             n_consonants += 1
#     return n_vowels, n_consonants
#
# amongus= "amongus"
# print(char_counts(amongus))

#Variable Number of Arguments
# def mean(*args):
#     tot = 0
#     for a in args:
#         tot += a
#     return tot/len(args)
#
# print(mean(6,8,7,7,4,3,2,5,6,7,8))

#sum_and_product task
# def sum_and_product(l):
#     """L is a list of numbers
#     Return a tuple where the first value is the sum of all elements in L and the second value is the product of all elements in L"""
#     sum = 0
#     prod = 1
#     for num in l:
#         sum += num
#         prod *= num
#     return sum, prod
#
# test = [1, 2, 3, 4, 5]
# print(sum_and_product(test))

#.append exercise
# L1 = ["re"]
# L2 = ["mi"]
# L3 = ["do"]
#
# L4 = L1 + L2
# L3.append(L4)
# L = L1.append(L3)
#
# print(L1)
# print(L2)
# print(L3)
# print(L4)
# print(L)

#make_ordered_list task
# def make_ordered_list(n):
#     """n is a positive int
#     Returns a list containing all ints in order from 0 to n (inclusive)"""
#     mylist = []
#     for i in range(n+1):
#         mylist.append(i)
#     return mylist
#
# print(make_ordered_list(9))

#remove_elem task
# def remove_elem(L, e):
#     """ L is a list
#     Returns a new list with elements in the same order as L but without any elements equal to e."""
#     new_list = []
#     for n in L:
#         if n != e:
#             new_list.append(n)
#     return new_list
#
# print(remove_elem([1, 2, 2, 5, 7, 8, 2, 4],2))

#count_words
# def count_words(sen):
#     """sen is a string representing a sentence
#     Returns how many words are in s (i.e. a word is a sequence of characters between spaces)."""
#     count_list = sen.split(" ")
#     return len(count_list)
#
# print(count_words("Hello it's me"))

#sort_words task
# def sort_words(sen):
#     """sen is a string representing a sentence
#     Returns a list containing all the words in sen but sorted in alphabetical order"""
#     list = sen.split(" ")
#     list.sort()
#     return list
#
# print(sort_words("today I'm enjoying the sun and the breeze".lower()))

#square_list task
# def square_list(mylist):
#     for i in range(len(mylist)):
#         mylist[i] = mylist[i]**2
#     return mylist
#
# print(square_list([1, 2, 3]))