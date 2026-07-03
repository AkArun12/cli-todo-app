# 📝 CLI To-Do App (Python)

A simple command-line To-Do application built using Python.
This project helps manage daily tasks directly from the terminal with features like adding, viewing, completing, and deleting tasks.

---

## 🚀 Features

* Add new tasks
* View all tasks
* Delete tasks
* Mark tasks as completed
* Persistent storage using JSON (tasks saved between sessions)
* Simple and beginner-friendly CLI interface

---

## 🛠️ Technologies Used

* Python 3
* JSON (for data storage)
* Command Line Interface (CLI)

---

## 📂 Project Structure

```
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
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/AkArun12/cli-todo-app.git
```

### 2. Navigate into the project

```bash
cd cli-todo-app
```

### 3. Run the program

```bash
python main.py
```

---

## 🧭 How to Use

Once the program starts, you'll see a menu like:

```
===== CLI TO-DO APP =====

1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Complete
5. Exit
```

### Example Workflow:

* Choose `1` → Enter a task name
* Choose `2` → View all tasks
* Choose `4` → Mark a task as completed
* Choose `3` → Delete a task
* Choose `5` → Exit program

---

## 💾 Data Storage

All tasks are stored in a `tasks.json` file.

Example format:

```json
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
```

---

## 📌 Future Improvements

* Add due dates for tasks
* Add priority levels (High / Medium / Low)
* Search and filter tasks
* Colorful terminal UI (using `rich`)
* Task statistics (completed vs pending)
* Unit tests with `pytest`
* Convert into a web app using Flask or FastAPI

---

## 🧠 What I Learned

* Python fundamentals (loops, functions, dictionaries)
* File handling and JSON
* Structuring a real-world Python project
* Building CLI applications
* Using Git and GitHub for version control

---

## 👨‍💻 Author

**Arun Kathariya**
GitHub: [https://github.com/AkArun12]

---



