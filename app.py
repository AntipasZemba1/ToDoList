# List to store tasks; each task is a dictionary with a description and completion status.
tasks[]

# Function to display the menu options to the user.
def show_menu():
    print("\n*** TO DO LIST ***")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark Task as COmpleted")
    print("1. Delete Task")
    print("1. Exit")

# Function to add a new task to the list
def add_task():
    task = input("Please enter a new task: ")
    tasks.append({"task":task, "done": False})
    print("Task added!")

# Function to display all tasks with their completion status
def view_tasks()
    if not tasks:
        print("No tasks in your list.") # To inform user if the list is empty
        for index, t in enumarate(tasks, start=1):
            # show ✅ for completed tasks, ❌ for incomplete
            status = "✅" if t ["done"] else "❌"
            print(f"{index}. {t['task']} [{status}]")

# Function to mark a specific as completed
def mark_completed():
    view_tasks()
    try:
        num = int(input("Please enter task number to mark as complete: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True # Set the "done" status to True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.") # Hundle non-integer input