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
        status="[X]" if task["completed"] else "[ ]"

        print(f"{index}. {status} {task['title']}")
       
        print("---------------------------------------")

#Function to save data:

def save_tasks(tasks):
    with open("tasks.json","w") as file:
        json.dump(tasks,file, indent=4)

def load_tasks():
    try:
        with open("tasks.json","r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
tasks=load_tasks()

#Function to delete task:

def delete_task(tasks):
    if len(tasks)==0:
        print("No tasks found!")
        return
    
    view_tasks(tasks)
    try:
        task_id=int(input("Enter the task ID to delete: "))
        if 1<= task_id<=len(tasks):
            deleted_task=tasks.pop(task_id -1)
            save_tasks(tasks)
            print(f"Task '{deleted_task['title']}' deleted successfully")

        else:
            print("Invalid task id")
    
    except ValueError:
        print("Please enter a valid number.")

# Function for task completion:

def mark_complete(tasks):
    if len(tasks)==0:
        print("No tasks found")
        return
    
    view_tasks(tasks)

    try:
        task_id=int(input("Enter a task number to mark as complete:"))
        if 1<=task_id<=len(tasks):
            tasks[task_id-1]["completed"]=True
            save_tasks(tasks)
            print("Task marked as completed")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number")



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
                print("You selected : Exit")
                break
            else:
                print("Invalid input.")
        except ValueError:
            print("Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
    


