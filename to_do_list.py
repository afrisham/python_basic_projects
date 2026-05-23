# Simple To-Do List App

tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks found!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

while True:
    print("\n--- TO DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()
        if len(tasks) > 0:
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"Deleted task: {removed}")
            else:
                print("Invalid task number!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
