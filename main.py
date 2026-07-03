import json
tasks=[]
def show_menu():
    print("\n=========================")
    print("CLI TO-DO APP")
    print("==========================")
    print("1. Add Task\n")
    print("2. View Task\n")
    print("3. Delete Task\n")
    print("4. Mark Complete\n")
    print("5. Exit\n")

#Function to Add Tasks.

def add_task(tasks):
    title=input("Enter the task: ")
    task={
            "id":len(tasks)+1,
            "title":title,
            "completed":False
        }
    tasks.append(task)
    print("Task added successfully!")

def view_tasks(tasks):
    if len(tasks)==0:
        print("No Tasks found.")
        return
    print("\n----------------------------------")

    for index, task in enumerate(tasks, start=1):
        status="completed" if task["completed"] else "Pending"

        print(f"{index}.")
        print(task["title"])
        print(f"Status :{status}")
        print("---------------------------------------")

#Function to save data:

def save_tasks(tasks):
    with open("tasks.json","w") as file:
        json.dump(tasks,file, indent=4)



def main():
    while True:
        show_menu()
        try:
            choice=int(input("Enter ypur choice: "))
            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                print("You selected : Delete Task")
            elif choice == 4:
                print("You selected : Mark Complete") 
            elif choice == 5:
                print("You selected : Exit")
                break
            else:
                print("Invalid input.")
        except ValueError:
            print("Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
    


