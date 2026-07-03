1. 📝 CLI To-Do App (Python)

A simple command-line To-Do application built using Python.
This project helps manage daily tasks directly from the terminal with features like adding, viewing, completing, and deleting tasks.

===================================================================
2. 🚀 Features
Add new tasks
View all tasks
Delete tasks
Mark tasks as completed
Persistent storage using JSON (tasks saved between sessions)
Simple and beginner-friendly CLI interface
===================================================================


3. 🛠️ Technologies Used
Python 3
JSON (for data storage)
Command Line Interface (CLI)
===================================================================

4. 📂 Project Structure

CLI-Todo-App/
│
├── main.py              # Main program (entry point)
├── task_manager.py      # Task operations (add, delete, complete, view)
├── storage.py           # Load/save tasks from JSON file
├── utils.py             # Helper functions (menu, validation, etc.)
├── tasks.json           # Data storage file
├── README.md            # Project documentation
├── .gitignore           # Files to ignore in Git
└── venv/                # Virtual environment (not pushed to GitHub)

===================================================================

5. ▶️ To Run
=> Clone the repository 
git clone https://github.com/AkArun12/cli-todo-app.git

=> Navigate in to the project :
 cd cli-todo-app

=> Run the program:
    python main.py

===================================================================

6. 🧭 How to Use

Once the program starts, you'll see a menu like:

===== CLI TO-DO APP =====

1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Complete
5. Exit
Example Workflow:
Choose 1 → Enter a task name
Choose 2 → View all tasks
Choose 4 → Mark a task as completed
Choose 3 → Delete a task
Choose 5 → Exit program

===================================================================

7. 💾 Data Storage

All tasks are stored in a tasks.json file.

Example format:

[
    {
        "id": 1,
        "title": "Learn Python",
        "completed": false
    },
    {
        "id": 2,
        "title": "Build CLI Project",
        "completed": true
    }
]
===================================================================

8. 📌 Future Improvements
Add due dates for tasks
Add priority levels (High / Medium / Low)
Search and filter tasks
Colorful terminal UI (using rich)
Task statistics (completed vs pending)
Unit tests with pytest
Convert into a web app using Flask or FastAPI
===================================================================

9. 🧠 What I Learned From This Project
Python fundamentals (loops, functions, dictionaries)
File handling and JSON
Structuring a real-world Python project
Building CLI applications
Using Git and GitHub for version control

10. 👨‍💻 Author
Arun Kathariya
GitHub: https://github.com/AkArun12
