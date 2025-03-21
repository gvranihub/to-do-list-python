tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks added yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def remove_task():
    show_tasks()
    try:
        task_num = int(input("Enter task number to remove: ")) - 1
        removed = tasks.pop(task_num)
        print(f"Task '{removed}' removed!")
    except (IndexError, ValueError):
        print("Invalid task number.")

while True:
    print("\nOptions: [1] Show Tasks  [2] Add Task  [3] Remove Task  [4] Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option!")

