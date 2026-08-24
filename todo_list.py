tasks = []


def add_task():
    task_name = input("Enter the task: ")

    task = {
        "name": task_name,
        "completed": False
    }

    tasks.append(task)

    print("Task added successfully!")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
        return

    print("\n----- YOUR TASKS -----")

    for i, task in enumerate(tasks, start=1):

        if task["completed"]:
            status = "Completed"
        else:
            status = "Pending"

        print(i, ".", task["name"], "-", status)


def complete_task():
    view_tasks()

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("Enter the task number to complete: "))

        if task_number >= 1 and task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True

            print("Task marked as completed!")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    view_tasks()

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("Enter the task number to delete: "))

        if task_number >= 1 and task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)

            print("Deleted task:", deleted_task["name"])

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


while True:

    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")
