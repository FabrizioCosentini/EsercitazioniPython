#Task on input and print commands
#Verb1=input("Write a verb: ")
#print("I can", Verb1, "better than you!")
#print (4*(Verb1+" ")+Verb1)

#Task on Newton's Method (on print and input)
#x=int(input("What x to find the cube root of? "))
#g=int(input("What guess to start with? "))
#print("Current estimate cubed = ", g**3)
#next_g=g-((g**3-x)/(3*g**2))
#print("Next guess to try = ", next_g)

#f-strings task
#num=3000
#fraction=1/3
#print(num*fraction, "is", fraction*100, "% of", num)
#print(num*fraction, "is", str(fraction*100) + "% of", num)
#print(f"{num*fraction} is {fraction*100}% of {num}")

#Guess the number? task
#secret = 8
#guess = int(input("What is your guessed number? "))
#print(guess == secret)

#If number task
#x = int(input("Enter a number for x: "))
#y = int(input("Enter a different number for y: "))
#if x==y:
#    print (x, "is the same as", y)
#    print ("These are equal!")

#If task 2
#x=float(input("Enter a number for x: "))
#y=float(input("Enter a number for y: "))
#if x == y:
#    print ("x and y are equal")
#    if y != 0:
#        print("therefore, x/y is", x/y)
#elif x < y:
#    print ("x is smaller")
#else:
 #   print ("y is smaller")
#print("thanks!")

#Guess too low, high, or equal task
#secret = 9
#guess = int(input("Try to guess my same number: "))
#if secret == guess:
#    print("You guessed my number!")
#elif guess < secret:
#    print("Too low!")
#else:
#    print("Too high!")

#Lost in the Forest task (refined)
#where = input ("You're lost in the forest. Go left or right? ")
#n_tries = 0
#while where.lower() != "left" and n_tries < 2:
#    if where.lower() == "right":
#        n_tries += 1
#        if n_tries < 2:
#            where = input("You're still lost in the forest. Go left or right? ")
#    else:
#        print("You can only go left or right.")
#        where = input ("Again, go left or right? ")
#if n_tries < 2:
#    print("You got out of the forest!")
#else:
#    print(":(")

#Non-integer Task
#n = int(input("Enter a non-negative integer: "))
#while n > 0:
#    print ("X")
#    n=n-1

#Factorial finder Task
#x = 4
#i = 1
#factorial = 1
#while i <= x:
#    factorial *=i
#    i +=1
#print(f"{x} factorial is {factorial}")

#Total sum Task
#mysum = 0
#start = 5
#end = 10
#for i in range (start, end+1):
#    mysum += i
#print(mysum)