# 📋 Task Tracker CLI

A simple command-line task tracking application built in Python.

This project was built as part of the roadmap.sh Backend Developer roadmap to practice Python fundamentals, file handling, JSON storage, and command-line interfaces.

---

## Features

- ✅ Add tasks
- ✅ Update task descriptions
- ✅ Delete tasks
- ✅ Mark tasks as **done**
- ✅ Mark tasks as **in progress**
- ✅ List all tasks
- ✅ Filter tasks by status (`todo`, `done`, `in-progress`)
- ✅ Persistent storage using a JSON file

---

## Technologies Used

- Python 3
- JSON
- Command Line Interface (CLI)

---

## Project Structure

```
Task-Tracker-cli/
│
├── task_cli.py
├── README.md
├── .gitignore
└── tasks.json (generated automatically)
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/Saltysnacc124/Task-Tracker-cli.git
```

Move into the project directory

```bash
cd Task-Tracker-cli
```

---

## Usage

### Add a task

```bash
python task_cli.py add "Buy groceries"
```

### List all tasks

```bash
python task_cli.py list
```

### List completed tasks

```bash
python task_cli.py list done
```

### List todo tasks

```bash
python task_cli.py list todo
```

### List tasks in progress

```bash
python task_cli.py list in-progress
```

### Update a task

```bash
python task_cli.py update 1 "Buy milk"
```

### Delete a task

```bash
python task_cli.py delete 1
```

### Mark a task as done

```bash
python task_cli.py mark-done 1
```

### Mark a task as in progress

```bash
python task_cli.py mark-in-progress 1
```

---

## Learning Outcomes

This project helped me practice:

- Python functions
- Command-line arguments (`sys.argv`)
- File handling
- JSON serialization/deserialization
- Lists and dictionaries
- CRUD operations
- Basic software design
- Refactoring and code organization

---

## Future Improvements

- Better input validation
- Colored terminal output
- Search tasks by keyword
- Due dates and priorities
- Unit tests
- Packaging as an installable CLI tool

---

## Acknowledgements

Project idea from:

https://roadmap.sh/projects/task-tracker