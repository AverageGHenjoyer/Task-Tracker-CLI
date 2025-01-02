# Task-Tracker-CLI with only sys.argv

Project idea from [roadmap.sh backend projects](https://roadmap.sh/projects/task-tracker).

Task Tracker CLI is a simple command-line task manager that allows you to add, update, delete, and view tasks stored in a JSON file.

## Features
- **Add new tasks** (`add`)
- **Update task descriptions** (`update`)
- **Delete tasks** (`delete`)
- **Mark tasks as "in progress" or "done"** (`mark-in-progress`, `mark-done`)
- **View task lists** (`list`, `list-done`, `list-in-progress`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/maciej3j/task-tracker-cli.git
   ```
2. Navigate to the project directory:
   ```bash
   cd task-tracker-cli
   ```
3. Ensure you have Python 3 installed.

## Usage

Run the program from the command line with the following commands:

### Add a new task
```bash
python main.py add "Task description"
```

### Update a task
```bash
python main.py  update TASK_ID "New task description"
```

### Delete a task
```bash
python main.py  delete TASK_ID
```

### Mark a task as "in progress"
```bash
python main.py  mark-in-progress TASK_ID
```

### Mark a task as "done"
```bash
python main.py mark-done TASK_ID
```

### List tasks
- All tasks:
  ```bash
  python main.py  list
  ```
- Tasks by status:
  ```bash
  python main.py  list todo
  python main.py  list in-progress
  python main.py  list done
  ```