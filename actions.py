import json
from datetime import datetime
import sys

def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(data):
    try:
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4, default=str)
    except IOError:
        print("Failed to save data.")


def validate_id(input_id):
    try:
        return int(input_id)
    except ValueError:
        print("Invalid ID. Please enter a numeric value.")
        sys.exit(1)


def generate_id(data):
    data = validate_id(data)
    if not data:
        return 1
    return max(item["ID"] for item in data) + 1


def task_add(description, status="todo"):
    new_task = {
        "ID": generate_id(data),
        "description": description,
        "status": status,
        "created_at": datetime.now().replace(microsecond=0),
        "updated_at": datetime.now().replace(microsecond=0)
    }

    data.append(new_task)
    save_data(data)


def task_list():
    if not data:
        print("No tasks found.")
        return
    if len(sys.argv) == 3:
        match(sys.argv[2]):
            case "done":
                for task in data:
                    if task['status'] == 'done':
                        print(f"ID: {task['ID']}, task: {task['description']}, status: {task['status']}")
            case "todo":
                for task in data:
                    if task['status'] == 'todo':
                        print(f"ID: {task['ID']}, task: {task['description']}, status: {task['status']}")

            case "in-progress":
                for task in data:
                    if task['status'] == 'in-progress':
                        print(f"ID: {task['ID']}, task: {task['description']}, status: {task['status']}")

            case _:
                print("Wrong option for task status.")
    elif len(sys.argv) == 2:
        for task in data:
            print(f"ID: {task['ID']}, task: {task['description']}, status: {task['status']}, created_at: {task['created_at']}, last_updated: {task['updated_at']}")

def task_update(ID, new_description):
    global data
    ID = int(ID)
    if not data:
        print("There is nothing to change.")
        return
    success = False
    for task in data:
        if task['ID'] == ID:
            task['description'] = new_description
            task['updated_at'] = datetime.now().replace(microsecond=0)
            success = True
    if success:
        save_data(data)
    else:
        print(f"Task with ID {ID} not found.")

def task_delete(ID):
    global data
    ID = int(ID)
    if not data:
        print("There is nothing to delete.")
        return
    original_length = len(data)
    updated_data = [item for item in data if item['ID'] != ID]
    new_length = len(updated_data)
    if new_length < original_length:
        print("Task has been successfully deleted.")
    else:
        print(f"Not found such task with ID {ID}.")

    save_data(updated_data)


def task_mark_in_progress(ID):
    global data
    ID = int(ID)
    if not data:
        print("There is nothing to change.")
        return
    success = False
    for task in data:
        if task['ID'] == ID:
            task['status'] = "in-progress"
            success = True
    if success:
        save_data(data)
    else:
        print(f"Task with ID {ID} not found.")


def task_mark_done(ID):
    global data
    ID = int(ID)
    if not data:
        print("There is nothing to change.")
        return
    success = False
    for task in data:
        if task['ID'] == ID:
            task['status'] = "done"
            success = True
    if success:
        save_data(data)
    else:
        print(f"Task with ID {ID} not found.")

