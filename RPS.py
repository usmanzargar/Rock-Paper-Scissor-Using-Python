import random


user_wins = 0
computer_wins = 0


choices = ["rock", "paper", "scissors"]



while True:
    user_input = input("Welcome to RPS! Please type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q" :
        break

    if user_input not in choices :
        continue


    random_rps = random.randint(0,2)
    

    computer_input = choices[random_rps]
    print("Computer's input: ", computer_input, ".")


    if user_input == "rock" and computer_input == "scissors" :
        print("Congratulations, you won! Rock smashes scissors.")
        user_wins += 1
       

    elif user_input == "paper" and computer_input == "rock" :
        print("Congratulations, you won! Paper covers rock.")
        user_wins += 1
        

    elif user_input == "scissors" and computer_input == "paper" :
        print("Congratulations, you won! Scissors cut paper")
        user_wins += 1

    elif user_input == computer_input :
        print("Looks like you & the computer are on the same page.")


    else :
        print("You lost!")
        computer_wins += 1


print("You won", user_wins, "times")
print("Computer won", computer_wins, "times")
print("Thank you for playing! Goodbye!")
        

    
        
