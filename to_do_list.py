print("Welcome to the To-Do List App!")
tasks = []
while True:
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")
choice = input("Enter your choice (1-4): ")
if choice == '1':
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")
elif choice == '2':
    if tasks:
        print("Your To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("Your To-Do List is empty.")
elif choice == '3':
    if tasks:
        print("Your To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
        try:
            task_num = int(input("Enter the number of the task you want to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' removed from the list.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Your To-Do List is empty.")