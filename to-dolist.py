import os
import json

# Function to load tasks from a JSON file
def load_tasks(filename):
    tasks = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            tasks = json.load(file)
    return tasks

# Function to save tasks to a JSON file
def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to display tasks
def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['title']} - {'Done' if task['done'] else 'Not Done'}")

# Function to add a new task
def add_task(tasks, title):
    tasks.append({"title": title, "done": False})

# Function to mark a task as done
def mark_task_done(tasks, index):
    if index >= 1 and index <= len(tasks):
        tasks[index - 1]["done"] = True
    else:
        print("Invalid task index.")

# Function to delete a task
def delete_task(tasks, index):
    if index >= 1 and index <= len(tasks):
        del tasks[index - 1]
    else:
        print("Invalid task index.")

# Main function
def main():
    filename = "tasks.json"
    tasks = load_tasks(filename)

    while True:
        print("\nTo-Do List Application")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            title = input("Enter task title: ")
            add_task(tasks, title)
            save_tasks(filename, tasks)
            print("Task added.")
        elif choice == '3':
            index = int(input("Enter the index of the task to mark as done: "))
            mark_task_done(tasks, index)
            save_tasks(filename, tasks)
            print("Task marked as done.")
        elif choice == '4':
            index = int(input("Enter the index of the task to delete: "))
            delete_task(tasks, index)
            save_tasks(filename, tasks)
            print("Task deleted.")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
