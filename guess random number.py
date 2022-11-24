#import random module
import random

#choose upper and lower limits.
#using the functions to ensure the value entered is an integer
upper_limit=int(input("enter upper limit\n"))
lower_limit=int(input("enter lower limit\n"))

#selects a rondom number between upper and lower boundry
random_number=random.randint(lower_limit,upper_limit)
print("\nyou will have to enter a number between ",upper_limit,"and",lower_limit)

#we assign variable "chances" that will acts as the counter to loop
chances=0
while(1):
    while chances<8:
        chances+=1
        guess=int(input("enter the guess:\n"))
        if random_number==guess:
            print("congrats!you did it,the number was",random_number)
            break
        elif guess<random_number:
            print("you guessed a small number\n")
        elif guess>random_number:
            print("you guessed a large number\n")
        if chances==7:
            print("you've ran out of chances\n")
            print("\nthe number was",random_number)
            print("\nbetter luck next time")
            break
    print("\n")
    break