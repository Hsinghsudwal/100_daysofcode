import random

rock = 'rock'
paper = 'paper'
scissors ='scissors'

while True:
    choice = input("What do you choose? Rock = 0, Paper =1 or Scissors = 2\n0/1/2:")
    computers_choice = random.randint(0,2)

    if not choice.isdigit():
        print("You've entered an invalid value, try again and choose a number between 0-2.")

    else:
        choice = int(choice)
        if choice > 2:
            print("You've entered an invalid number, try again and choose a number between 0-2.")
        elif choice == 0 or choice == 1 or choice == 2:
            if choice == 0:
                print(f"You chose: {rock}")
            elif choice == 1:
                print(f"You chose: {paper}")
            elif choice == 2:
                print(f"You chose: {scissors}")

        if computers_choice == 0:
            print(f"The computer chose: {rock}")
            if choice == 2:
                print("You lose, Rock wins scissors.")
            elif choice == 0:
                print("It's a draw!")
            else:
                print("You win!")

        elif computers_choice == 1:
            print(f"The computer chose: {paper}")
            if choice == 0:
                print("You lose, Paper wins rock.")
            elif choice == 0:
                print("It's a draw!")
            else:
                print("You win!")

        elif computers_choice == 2:
            print(f"The computer chose: {scissors}")
            if choice == 1:
                print("You lose, Scissors win against paper.")
            elif choice == 2:
                print("It's a draw!")
            else:
                print("You win!")


