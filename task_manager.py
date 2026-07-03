from storage import save_tasks

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
    print("\n----------------------------------------")

    for index, task in enumerate(tasks, start=1):
        status="[X]" if task["completed"] else "[ ]"

        print(f"{index}. {status} {task['title']}")
       
        print("---------------------------------------")




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

