# All-In-One Terminal App
                                         # ==========MENU========== #                   
#MAIN MENU:

def main_menu():
    clear_screen()
    print(f"\n👋 Hello! Welcome to your All-In-One Terminal App 💻?")
    print("1. Calculate")
    print("2. Note ")
    print("3. Game ")
    print("4. Exit")
   
                                        # ==========ACTION========== #    
#Action menu:
def action_menu():  
    while True:
        try:
            while True: 
                
                choice = input("Please enter your choice: ")
                
                if choice in ("1","2","3","4"):
                    break
                
                else:
                    print("invalid input or choice! try again.")
            
            if choice == "1":
                calculate_menu()          
                action_calculate()
                break  
                                      
            elif choice == "2":
                import todo 
                break
                
            elif choice == "3":
                game_menu()
                action_game()
                break
                
            elif choice == "4":
                print("Goodbye!")
                break
        
            else:
                print("Invalid choice!")
                
        except Exception as e:
            print(f"An error occurred: {e}")

#CALCULATE MENU:
def calculate_menu():
    clear_screen()
    print("\n=====Calculate Menu=====")
    print("1. Calculate BMI,")
    print("2. Calculator (opperations: -, +, *, /, **, //, %) , Just two numbers.")
    print("3. Calculate your age in days, months, years.")
    print("4. Return to main menu.")
    print("5. Exit.")
        
#Action calculate:
def action_calculate():
    while True:
        try:
            while True:
                
                first_choice = input("Please enter your choice: ")
                
                if first_choice in ("1","2","3","4","5"):
                    break
                
                else:
                    print("invalid input or choice! try again.")
                    
            if first_choice == "1":
                calculate_bmi()
                        
            elif first_choice == "2":
                calculator()
            
            elif first_choice == "3":
                calculate_age()
            
            elif first_choice == "4":
                restart()
                
            elif first_choice == "5":
                print("Goodbye!")
                break
                
            else:
                print("Invalid choice!")
                    
        except ValueError: 
            print("Invalid input! try again. ")
            
        except Exception as e:
            print(f"An error occurred: {e}")
            
            

#GAMES MENU:
def game_menu():
    clear_screen()
    print("\n=====Games Menu=====")
    print("1. Guessing game. ")
    print("2. Rock, Paper, Scissors. ")
    print("3. Return to the main menu. ")
    print("4. Exit. ")
    
#ACTION GAME:
def action_game():
    while True:
        try:
            while True:
                
                second_choice = input("Please enter your choice: ")
                if second_choice in ("1","2","3","4"):   
                    break
                
                else:
                    print("invalid input or choice! try again.")
                    
            if second_choice == "1":
                import guessbyMe   
                game_menu()
                action_game()
                         
            elif second_choice == "2":
                import rps_game
                game_menu()
                action_game()
                
            elif second_choice == "3":
                restart()
                
            elif second_choice == "4":
                print("Goodbye!")
                break
                
        
            else:
                print("Invaid choice")
        
        except Exception as e:
            print(f"An error occurred: {e}")
        
                                        # ==========OTHER FUNCTIONS========== #

import os                                      
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


#CALCULATE BMI
def calculate_bmi():
    while True:
        try:
            while True:
                try:
                    
                    weight = float(input("Enter your weight in kg: "))
                    break
                
                except ValueError: 
                    print("Invalid input!")     
                
            while True:
                try:   
                    
                    height = float(input("Enter your height in meters: "))
                    break
                
                except ValueError: 
                    print("Invalid input!")
                    
            bmi = weight / (height ** 2)
            print(f"Your BMI is: {bmi}")
        
            if bmi < 18.5:
                print("You are underweight.")
            
            elif 18.5 <= bmi < 24.9:
                print("You have a normal weight.")
            
            elif 25 <= bmi < 29.9:
                print("You are overweight.")
            
            else:
                print("You are obese.")
                
            while True:
                
                again = input("Do you want to use BMI calculator again(yes/no)?: ").lower().strip()
                
                if again in ("yes" , "no"):
                    break
                
                else:
                    print("Please enter 'yes' or 'no'. ")
        
            if again != "yes":
                calculate_menu()
                action_calculate()
                
        except Exception as e :
            print(f"An error occurred: {e}")
        
        
        
        
#calculator fonctions:      
def add(a, b):
    return a + b

def subtract(a, b):
     return a - b
 
def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b):
    return a ** b

def remainder(a,b):
    return a % b

def floor_divide(a, b):
    return a // b

def calculator():
    while True:
        try:  
            while True:
                try:
                    
                    a = float(input("Enter the first number: "))
                    break
                
                except ValueError : 
                    print("Please enter a number!")
                    
            while True:
                try:
                    
                    b = float(input("Enter the second number: "))
                    break
                
                except ValueError : 
                    print("Please enter a number!")
                    
            while True:
                
                    op = input("Enter the operation : ")
                    if op in ["+", "-", "*", "/", "**", "%", "//"]:
                        break
                    
                    else:
                        print("Invalid operation! Please try again.")   
                                    
            if op == "+":
                result = add(a,b)
                
            elif op == "-":
                result = subtract(a,b)
                
            elif op == "*":
                result = multiply(a,b)
                
            elif op == "/":
                result = divide(a,b)
                
            elif op == "**":
                result = power(a,b)
                
            elif op == "%":
                result = remainder(a,b)
                
            elif op == '//':
                result = floor_divide(a,b)
                
            print(f"\nResult : {result}")
            
            while True:
                
                again = input("\n Do you want to use calculator again?(yes/no): ").lower().strip()
                
                if again in ("yes", "no"):
                    break
                
                else:
                    print("Please enter 'yes' or 'no'.")
                
            if  again != "yes":
                print("Goodbye!")
                break
            
            else:
                continue
            
        except ZeroDivisionError : 
            print("Error: Cannot divide by zero!")
            
        except Exception as e :
            print("Unexpected error:", e)
        
#CALCULATE AGE 
def calculate_age():
    while True:
        try:
            while True:
                try:
                    
                    year = int(input("What's your date of birth?: "))
                    
                except ValueError:
                    print("Invalid input! try again.")
                    continue
                
                age_yrs = 2025 - year
            
                age_mnts = age_yrs*12
            
                age_dys = age_mnts*30
     
                print(f"Your age in years is {age_yrs} ,in months {age_mnts} ,in days {age_dys} . (The result it's not exact!)")
            
                while True:
                
                    again = input("Do you want to use AGE calculator again(yes/no)?: ").lower().strip()
                
                    if again in ("yes", "no"):
                        break
                
                    else:
                        print("Please enter 'yes' or 'no'.")
                    
                if again != "yes":
                    calculate_menu()                    
                    action_calculate()                       
                          
        except Exception as e :
            print("Unexpected error:", e)

                                        # ==========MAIN PROGRAM STARS HERE========== #

def  restart():
    main_menu()
  
    try:
        action_menu()
        
    except ValueError: 
        print("Invalid input! try again.")
            
    except Exception as e :
        print("Unexpected error:", e)
        
if __name__ == "__main__":
    restart()
