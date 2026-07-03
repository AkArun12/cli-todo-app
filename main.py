from storage import load_tasks, save_tasks
from task_manager import (
    add_task,
    view_tasks,
    delete_task,
    mark_complete
)

from utils import show_menu
tasks= load_tasks()

#Function to Add Tasks.



def main():
    while True:
        show_menu()
        try:
            choice=int(input("Enter your choice: "))
            if choice == 1:
                add_task(tasks)
                save_tasks(tasks)
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                delete_task(tasks)
            elif choice == 4:
                mark_complete(tasks)
            elif choice == 5:
                print("Good bye!")
                break
            else:
                print("Invalid input.")
        except ValueError:
            print("Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
    


