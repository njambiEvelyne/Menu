 # elif choice == 2:
    #     print("\t\t\tYour Tasks")
    #     if not tasks:
    #         print("No tasks available!")
    #     else:
    #         for i, task in enumerate(tasks, start=1):
    #             status = "✔️" if task["completed"] else "❌"
    #             print(f"{i}. {task['task']} - {status}")

    # elif choice == 3:
    #     print("\t\t\tMark Task as Complete")
    #     if not tasks:
    #         print("No tasks available to mark as complete!")
    #     else:
    #         for i, task in enumerate(tasks, start=1):
    #             print(f"{i}. {task['task']} - {'✔️' if task['completed'] else '❌'}")
    #         try:
    #             task_number = int(input("Enter the task number to mark as complete: ")) - 1
    #             if 0 <= task_number < len(tasks):
    #                 tasks[task_number]["completed"] = True
    #                 print("Task marked as complete!")
    #             else:
    #                 print("Invalid task number.")
    #         except ValueError:
    #             print("Please enter a valid number.")

    # elif choice == 4:
    #     print("Exiting the program. Goodbye!")
    #     break

    # else:
    #     print("Invalid choice. Please enter a number between 1 and 4.")

