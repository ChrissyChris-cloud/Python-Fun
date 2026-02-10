def display_menu():
    print("To-Do List Menu:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. View all tasks")
    print("4. Exit")

def main():
    tasks = []  # List to store tasks

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter the task: ")
            tasks.append(task)
            print(f"Task '{task}' added.")
        elif choice == '2':
            try:
                index = int(input("Enter the index of the task to remove: "))
                removed_task = tasks.pop(index)
                print(f"Task '{removed_task}' removed.")
            except (IndexError, ValueError):
                print("Error: Invalid task index.")
        elif choice == '3':
            if tasks:
                print("Your tasks:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")
            else:
                print("No tasks to display.")
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please choose between 1-4.")

if __name__ == "__main__":
    main()
