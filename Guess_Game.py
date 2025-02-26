import random
Chance=0

# Generate a random number
num=random.randint(1,100)

# Loop for a maximum of 5 chances
while (Chance <5):
    try:
        # ask the user to rake a guess
        Guess=int(input("Guess a number between 1 and 100: "))
        
        # if the number more than guess
        if Guess>num:
            print("Too high ")

        # if the number less than guess
        elif Guess<num:
            print("Too low ")

        # if the number equal to guess
        else:
            print("well done! you Guessed the number ")
            break
        # update the chance
        Chance +=1

    except ValueError:
        # if the number is not valid 
        print("please enter a valid number ")

# If the user uses up all 5 chances
if(Chance==5):
    print("GAME OVER ! The correct number was ",num)
