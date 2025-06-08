# Restarted

# List to store tasks; each task is a dictionary with a description and completion status.

# Function to display the menu option
def show_menu():
    print("\n=== TO DO LIST ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

# Function to add a new task to the list
def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")

