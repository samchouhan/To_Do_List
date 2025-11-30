import os
import json

FILE_NAME = "tasks.json"

# Load existing tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks():
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

# Display menu
def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')  # clear console
    print("===================================")
    print("         📝 TO-DO LIST APP         ")
    print("===================================")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")
    print("===================================")

# View tasks
def view_tasks():
    os.system('cls' if os.name == 'nt' else 'clear')
    if not tasks:
        print("\nNo tasks found!\n")
    else:
        print("\nYour Tasks:\n")
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task['done'] else "❌"
            print(f"{i}. {task['title']} [{status}]")
    input("\nPress Enter to continue...")

# Add a new task
def add_task():
    title = input("Enter new task: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks()
        print(f"✅ '{title}' added!")
    else:
        print("⚠️ Task cannot be empty!")
    input("\nPress Enter to continue...")

# Mark a task as done
def mark_done():
    view_tasks()
    try:
        num = int(input("\nEnter task number to mark as done: "))
        tasks[num - 1]["done"] = True
        save_tasks()
        print("✅ Task marked as done!")
    except (ValueError, IndexError):
        print("⚠️ Invalid input!")
    input("\nPress Enter to continue...")

# Delete a task
def delete_task():
    view_tasks()
    try:
        num = int(input("\nEnter task number to delete: "))
        removed = tasks.pop(num - 1)
        save_tasks()
        print(f"🗑️ Removed '{removed['title']}'")
    except (ValueError, IndexError):
        print("⚠️ Invalid input!")
    input("\nPress Enter to continue...")


# MAIN PROGRAM
tasks = load_tasks()

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("\nGoodbye! 👋")
        break
    else:
        print("⚠️ Invalid choice!")
        input("\nPress Enter to continue...")
