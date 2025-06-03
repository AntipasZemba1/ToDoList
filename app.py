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