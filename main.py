import sys
import json

ERROR = '''Usage:
task-tracker-cli add "something"
task-tracker-cli mark-in-progress ID
task-tracker-cli mark-done ID
task-tracker-cli list
task-tracker-cli list-done
task-tracker-cli list-in-progress
task-tracker-cli update ID "something"
task-tracker-cli delete ID '''

try:
    if sys.argv[1]:
        pass
except IndexError:
    print(ERROR)
    sys.exit(1)

try:
    with open("data.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    data = []

def generate_id(data):
    if not data:
        return 1
    return max(item["ID"] for item in data) + 1


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
            success = True
    if success:
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
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

    with open("data.json", "w") as f:
        json.dump(updated_data, f, indent=4)

def get_object(ID):
    for task in data:
        if task['ID'] == ID:
            return task

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
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
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
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
    else:
        print(f"Task with ID {ID} not found.")


match(sys.argv[1]):
    case "add":
        try:
            task_add(sys.argv[2])
        except IndexError:
            print(ERROR)

    case "list":
        task_list()

    case "update":
        try:
            task_update(sys.argv[2], sys.argv[3])
        except IndexError:
            print(ERROR)

    case "delete":
        try:
            task_delete(sys.argv[2])
        except IndexError:
            print(ERROR)

    case "mark-in-progress":
        try:
            task_mark_in_progress(sys.argv[2])
        except IndexError:
            print(ERROR)

    case "mark-done":
        try:
            task_mark_done(sys.argv[2])
        except IndexError:
            print(ERROR)

    case _:
        print(ERROR)
