import random
print("\n*********************")
print("Number Guessing Game")
print("*********************")
number=random.randint(1,9)
chance=0
while chance<5:
    guess=int(input("\nGuess a number between 1 and 9:"))

    if(guess==number):
        print("\n**************************")
        print("Congratulations You Won!!!")
        print("**************************")
        break
    elif(guess<number):
        print("\n Your guess was incorrect. Guess a number higher than ",guess)
    elif(guess>number):
        print("\n Your guess was incorrect. Guess a number less than ",guess)
    chance+=1    
if chance>4:
    print("\n**************************************") 
    print("You Lose!!!. The correct number was ",number)
    print("**************************************")