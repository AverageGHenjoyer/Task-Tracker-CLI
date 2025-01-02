from actions import *
from json import JSONDecodeError

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
except (FileNotFoundError, JSONDecodeError):
    data = []


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
