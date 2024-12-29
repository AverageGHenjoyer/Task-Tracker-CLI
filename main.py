import sys
import json

try:
    with open("data.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    data = []

def generate_id(data):
    if not data:
        return 1
    return max(item["id"] for item in data) + 1


def task_add(description, status="in-progress"):
    new_task = {
        "ID": generate_id(data),
        "description": description,
        "status": status
    }

    data.append(new_task)
    with open("data.json", "w") as f:
        json.dump(data, f,indent=4)
        print("Task added successfully.")


def task_list():
    if not data:
        print("No tasks found.")
        return

    for task in data:
        print(f"ID: {task['ID']}, task: {task['description']}, status: {task['status']}")



ERROR = '''Usage:
task-tracker-cli add "something"
task-tracker-cli mark-in-progress ID
task-tracker-cli mark-done ID
task-tracker-cli list
task-tracker-cli list-done
task-tracker-cli list-in-progress
task-tracker-cli update ID "something"
task-tracker-cli delete ID '''

match(sys.argv[1]):
    case "add":
        try:
            task_add(sys.argv[2])
        except IndexError:
            print(ERROR)

    case "list":
        task_list()

    # case "mark-in-progress":
    #     try:


    case _:
        print(ERROR)
