#score = int(input("Enter your score (0-100): "))
#if score >= 90: 
#    print("A")
#elif score >= 80:
#    print("B")   
#elif score >= 70:
#    print("C")   
#elif score >= 60:
    #print("D")
#else:
    #print("F")


#n = int(input ("Enter a number: "))
#sum_even = 0

#for number in range(1, n+1):
    #if number % 2 == 0:
     #   sum_even += number
#print("Sum of even numbers:", sum_even)

#n = int(input ("Enter a starting number: "))
#while n > 1:
    #print(n)
    #n -= 1

#print("Blast off!")

#n = int( input( "Enter the size of the multiplication table: "))

#for i in range(1, n+1):
    #for j in range(1, n+1):
        #print( i * j, end="\t" )
    #print()

import random

secret = random.randint(1,100)
guess = 0

while guess != secret:
    guess = int(input("Guess a number 1-100: "))

    if guess > secret:
        print("Too high!")
    elif guess < secret:
        print("Too low!")
    else:
        print(f"Correct! The number was {secret}.")


