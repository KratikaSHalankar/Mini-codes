import random

#counter that track the number of times the dice rolled
counter=0

#infinite loop
while True:
    #asking the user to enter his choice(yes or no)
    choice=input('Want to Roll the Dice ?(Y or N): ')
    
    #if the user enters yes ,then
    if choice=='Y'or choice=='y':
        # Asking the user to enter the number of dice they want to roll
        num=int(input("How many Dice you want to Roll?: "))
        for i in range(num):
        #   rool the dice and generate random number
            Dice=random.randint(1,6)
        #   print the number
            print(f'{Dice}')
    #   updates the number of counter
        counter +=1
        print(f'You have rolled the dice {counter} time during this session.')


    #if the user enters no ,then
    elif choice=="N" or choice=='n':
        #   print a message
        print("GAME OVER!")
        #   then the program will terminate
        break

    # if the choice is other than (yes or no) then
    else:
        #   print invlid choice
        print("Invalid choice!")
