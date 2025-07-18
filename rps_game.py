import random

choices = ["Rock", "Paper", "Scissors"]
  
def RPS_game():
    print("\n---Welcome to the Rock, Paper, Scissors game!---")
    score = 0 
    while True:
        try:           
            while True:
                user_choice = input("Enter Rock, Paper, or Scissors : ").strip().capitalize()
                if user_choice in choices:
                    break
                else:    
                    print("Invalid choice!")
                    
            computer_choice = random.choice(choices)
            print(f"Computer chose: {computer_choice}")
            
            if user_choice == computer_choice:
                print("It's a tie!")                
                
            elif (user_choice == "Rock" and computer_choice == "Scissors") or \
                 (user_choice == "Paper" and computer_choice == "Rock") or \
                 (user_choice == "Scissors" and computer_choice == "Paper"):
                print("You win!")
                score += 1
                   
            else:
                print("You lose!")
                score -= 1
             
            while True:      
                cont = input("Do you want to play another round? (yes/no): ").strip().lower() 
                if cont in ('yes' , 'no'):
                    break
                    
                else:
                    print("Please enter 'yes' or 'no'.")
                    
            if cont == 'no':
                print("\nYour final score is:", score)
                
                while True:
                    again = input("Do you want to restart the game? (yes/no): ").strip().lower()
                    if again in ('yes', 'no'):
                        break
                    else:
                        print("Please enter 'yes' or 'no'.")
                        
                if again == 'no':
                    print("Goodbye!")
                    break
                
                else:
                    score = 0
                    continue

        except Exception as e :
            print(f"An error occurred: {e}")

RPS_game()