from greet import greet

# Testing the greet function
print(greet("User"))

# Function to display the menu
def display_menu():
    print("\n\t\t\tTASK MANAGER")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task as complete")
    print("4. Exit")

# Main Program
tasks = []  # Task list to store tasks

while True:
    display_menu()  # Display the menu
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        continue

    if choice == 1:
        print("\t\t\tAdding a Task")
        task = input("Enter the task: ")
        tasks.append({"task": task, "completed": False})
        print("Task added successfully!")

    elif choice == 2:
        print("\t\t\tYour Tasks")
        if not tasks:
            print("No tasks available!")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "✔️" if task["completed"] else "❌"
                print(f"{i}. {task['task']} - {status}")

    elif choice == 3:
        print("\t\t\tMark Task as Complete")
        if not tasks:
            print("No tasks available to mark as complete!")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['task']} - {'✔️' if task['completed'] else '❌'}")
            try:
                task_number = int(input("Enter the task number to mark as complete: ")) - 1
                if 0 <= task_number < len(tasks):
                    tasks[task_number]["completed"] = True
                    print("Task marked as complete!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == 4:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

