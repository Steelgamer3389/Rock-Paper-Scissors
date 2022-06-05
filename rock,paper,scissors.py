import random
c="y"
while c=="y":
    playerinp=input("Enter your choice(rock,paper,scissors): ")
    possiblech=["rock","paper","scissors"]
    computerch=random.choice(possiblech)
    print("You chose",playerinp,"The computer chose",computerch)
    
    if playerinp==computerch:
        print("Both players selected",playerinp,". It's a tie!")
    elif playerinp=="rock":
        if computerch=="scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif playerinp=="paper":
        if computerch=="rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif playerinp=="scissors":
        if computerch=="paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    playagain=input("Play again? (y/n): ")
    if playagain.lower() != "y":
        break
    else:
        c="y"
