import random

def play_round(low, high, score):
    secret = random.randint(low, high)
    attempts, max_attempts = 0, 5
    print(f"I'm thinking of a number between {low} and {high}.")
    while attempts < max_attempts:
        try:
            guess = int(input(f"{max_attempts-attempts} tries left. Your guess: "))
            attempts += 1
        except ValueError:
            print("Please enter an integer.")
            continue
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print("Correct!")
            score += 1
            break
    else:
        print(f"Out of tries! The number was {secret}.")
        score -= 1

    print("Your score is", score)
    return score

def main():
    score = 0
    print("Welcome to the Guessing Game!")
    while True:
        score = play_round(1, 10, score)
        while True:
            cont = input("Do you want to play harder round? (yes/no): ").strip().lower()
            if cont in ('yes', 'no'):
                break
            else:
                print("Please enter 'yes' or 'no'.")
        if cont == 'no':
            print("Thanks for playing! Final score:", score)
            break
        score = play_round(1, 20, score)
        while True:
            again = input("Do you want to play again? (yes/no): ").strip().lower()
            if again in ('yes', 'no'):
                break
            else:
                print("Please enter 'yes' or 'no'.")
        if again == 'no':
            print("Thanks for playing! Final score:", score)
            break

main()
        
        
  