print("Welcom To Tech Quiz")

Answer = input("Do you want to play the quiz? (yes/no): ").lower()
if Answer == "yes":
    print("Great! Let's start the quiz.")
    point=0
    print("You will get 1 point for each correct answer.\n")
else:
    print("Okay, maybe next time.")
    exit()

Question1=input("1.- Who is credited with inventing the World Wide Web? ")
if Question1.lower()=="tim berners-lee":
    print("Correct!\n")
    point+=1
else:
    print("Incorrect! The correct answer is Tim Berners Lee.\n")

Question2=input("2.- What does the acronym 'HTTP' stand for? ")
if Question2.lower()=="hypertext transfer protocol":
    print("Correct!\n")
    point+=1
else:
    print("Incorrect! The correct answer is Hypertext Transfer Protocol.\n")  

Question3=input("3.- What is the name of the programming language created by Guido van Rossum? ")
if Question3.lower()=="python":
    print("Correct!\n")
    point+=1
else:
    print("Incorrect! The correct answer is Python.\n")

Question4=input("4.- What does 'CSS' stand for? ")
if Question4.lower()=="cascading style sheets":
    print("Correct!\n")
    point+=1
else:
    print("Incorrect! The correct answer is Cascading Style Sheets.\n")

Question5=input("5.- What is the full form of USB? ")
if Question5.lower()=="universal serial bus":
    print("Correct!\n")
    point+=1
else:
    print("Incorrect! The correct answer is Universal Serial Bus.\n")

print("You have completed the quiz!")
print(f"You scored {point} out of 5.")

if point>=3:
    print("Congratulations! You passed the quiz.")
else:
    print("Sorry, you did not pass the quiz. Better luck next time!")
print("Thanks for participating!")
