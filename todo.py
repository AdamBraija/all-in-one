tasks = []
def add_task():    
        task = input("Enter a new task: ").strip()
        if task == "" :
            print("Task cannot be empty!")
        else:
            tasks.append({"Task" : task ,
                  "Status" : "Pending"})
            print("Task added.")
            choices_in_def()
               
def show_tasks():
    if not tasks :
        print("There is no tasks yet. ")
        return
    for i , task in enumerate(tasks,1):
        print(i,"-", end= " ")
        for key , value in task.items():                
            print(f" {key} : {value}")
               
def complete_task():  
    try:                 
        num_task_complete = int(input("Enter the number of the task you want to set it complete: "))               
        if 1 <= num_task_complete <= len(tasks):
            tasks[num_task_complete - 1]["Status"] = "Complete"
            print ("Task marked as complete.")
            print(tasks[num_task_complete - 1])            
        else:
            print("Task not found!")
    except ValueError :
        print("Invalid input! try again.")  
            
def delete_task():
    try:   
        num_task_del = int(input("Enter the number of the task you want to delete it: "))
        if 1 <= num_task_del <= len(tasks):
            removed = tasks.pop(num_task_del - 1)
            print ("Task removed: ", removed)           
        else:
            print("Task not found!")
    except ValueError :
        print("Invalid input! try again.") 
    
def edit_task():
    try:
        num_task_edit = int(input("Enter the number of the task you want to edit it: "))
        if 1 <= num_task_edit <= len(tasks):
            tasks[num_task_edit - 1]["Task"] = input("Edit task: ")
            print ("Task edited.")
            print(tasks[num_task_edit - 1])
        else:
            print("Task not found!")
    except ValueError :
        print("Invalid input! try again.") 
    
def choices_in_def():
    try:
        print("1- Return to the main menu.")
        print("2- Exit.")
        choice_def = int(input("Enter your choice: "))
        if choice_def == 1 :
            main()
        elif choice_def == 2 :
            print("Goodbye")
        else: 
            print("Invalid choice.")
    except ValueError:
        print("Invalid input!")        

def main():
    print("\n ======To-Do List======")
    print("1- Add task. ")
    print("2- Show tasks. ")
    print("3- Complete tasks. ")
    print("4- Delete task. ")
    print("5- Edit task. ")
    print("6- Return to the main menu. ")
    print("7- Exit. ")
    while True:
        try:         
            choice = input("Enter your choice: ")
            if choice == "1" :
                add_task()
            elif choice == "2" :
                show_tasks()
                choices_in_def()
            elif choice == "3" :
                show_tasks()
                if not tasks :
                    choices_in_def()
                complete_task()               
            elif choice == "4" :
                show_tasks()
                if not tasks :
                    choices_in_def()
                delete_task()   
            elif choice == "5" :
                show_tasks()
                if not tasks :
                    choices_in_def()
                edit_task()
            elif choice == "6" :
                from all_in_one import restart
                restart()
            elif choice == "7" : 
                print("Goodbye!")
                break
            else :
                print("Invalid choice! ")        
        except ValueError: 
            print("Please enter a valid choice.")
        except Exception as e:
            print(f"An error occurred: {e}")


main()