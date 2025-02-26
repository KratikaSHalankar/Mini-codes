import random

choices=('r','p','s')
while True:
    # ask user to make choice
    user_choice=input("Rock, Paper, or Scissors?(r/p/s): ").lower()
    # if choice is not valid
    if user_choice not in choices:
        print('Invalid choice !')
        continue

    # computer to make choice
    computer_choice=random.choice(choices)

    print(f'\tyou chosed {user_choice} ')
    print(f'\tcomputer chosed {computer_choice}')

    # determine the winner
    if user_choice==computer_choice:
        print("it's a tie ")
    elif (
        (user_choice == 'r' and computer_choice =='s') or
        (user_choice == 'p' and computer_choice == 'r') or
        (user_choice == 's' and computer_choice == 'p')):
        print('   HURRAY !! Victory is yours.   ') 
    else:
        print(" ---GAME OVER--- *Computer won the game*")
    
    # ask the user if they want to continue
    conclusion=input("want to continue the game (y/n): ").lower()
    # if not terminate
    if (conclusion== 'n'):
        print("THANK YOU FOR PLAYING")
        break
