
#TamarraJP4
#Programmer: Joshua Tamarra
#Email: jtamarra@cnm.edu
#Purpose: reate a text-based rock, paper, scissors game

#Imported random for random comp_choice
import random

#list
choice = ['rock', 'paper', 'scissors']

#rounds; Best of 3
rounds = 0

#score board
user_score = 0
comp_score = 0

#Welcome message
print("!! ROCK  PAPER // SCISSORS !!\n")

#while loop for game
while True:
    user = input("Choose either 'Rock', 'Paper', or 'Scissors': ").lower() #.lower() in case user types it in capitalized or mistakenly types a character in caps.
    
    comp_choice = random.choice(choice) #rng for computer

    print(f"\nYou chose {user}, computer chose {comp_choice}.\n") #display
    if user == comp_choice:
        print(f"Both players chose {user}. It's a tie!")
        print("score:",user_score, "/", comp_score)
        
    elif user == "rock":
        if comp_choice == "scissors":
            print("You won! Rock beats scissors!")
            user_score += 1
            print("score:",user_score, "/", comp_score)
        else:
            print("You lost.. Paper covers rock.")
            comp_score += 1
            print("score:",user_score, "/", comp_score)
    elif user == "paper":
        if comp_choice == "rock":
            print("You won! Paper covers rock!")
            user_score += 1
            print("score:",user_score, "/", comp_score)
        else:
            print("You lost.. Scissors cut paper.")
            comp_score += 1
            print("score:",user_score, "/", comp_score)
            
    elif user == "scissors":
        if comp_choice == "paper":
            print("You won! Scissors cut paper!")
            user_score += 1
            print("score:",user_score, "/", comp_score)
        else:
            print("You lost.. Rock beats scissors.")
            comp_score += 1
            print("score:",user_score, "/", comp_score)

    if user_score == 2:
        print("You win!")
        print("Final score:",user_score," - ",comp_score)
        again = input("Again, (y/n)? ").lower()
        if again == "y":
            user_score, comp_score = (0,0)
            continue
        elif again == "n":
            print("Ok bye")
            break
    elif comp_score == 2:
        print("You lost, nice try.")
        print("Final score:",user_score," - ",comp_score)
        again = input("Again, (y/n)? ").lower()
        if again == "y":
            user_score, comp_score = (0,0)
            continue
        elif again == "n":
            print("Ok bye")
            break
        
