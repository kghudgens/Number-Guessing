import random


computerChoice = random.randint(1,10)

print("Welcome to the Python Number Guessing Game.")
guess = input("Please guess what number the computer has selected between 1 and 10? ")
guess = int(guess)

def comparison(comp, user):
    #if guess is correct
    print("Your guess is " + str(user)+".")
    global secondGuess
    if comp == user:
        print("You guessed correctly. The computer selected " + str(comp))
    else:
        if comp > user:
            print("The computer's selection was higher than yours.")
        if comp< user:
            print("Your selection was too high.")
        print("Your guess was incorrect. Please choose again.")
        secondGuess = input()
        secondGuess = int(secondGuess)
        


def comparison2(comp, user):
    print("Your guess is " + str(user)+".")
    global thirdGuess
    if comp == user:
        print("You guessed correctly. The computer selected " + str(comp))
    else:
        if comp > user:
            print("The computer's selection was higher than yours.")
        if comp< user:
            print("Your selection was too high.")
        print("Your guess was incorrect. Please choose again.")
        thirdGuess = input()
        thirdGuess = int(thirdGuess)
        


def comparison3(comp, user):
    print("Your guess is " + str(user) + ".")
    if comp == user:
        print("You guessed correctly. The computer selected " + str(comp))
    else:
        print("You were wrong again. The computer selected: " + str(comp))
    

comparison(computerChoice, guess)
comparison2(computerChoice, secondGuess )
comparison3(computerChoice, thirdGuess)