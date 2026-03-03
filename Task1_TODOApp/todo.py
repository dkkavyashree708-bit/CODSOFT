import json
import os


class TodoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from file"""
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

    def save_tasks(self):
        """Save tasks to file"""
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, title):
        task = {
            "title": title,
            "completed": False
        }
        self.tasks.append(task)
        self.save_tasks()
        print("✅ Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("📭 No tasks available.")
            return

        print("\nYour To-Do List:")
        for index, task in enumerate(self.tasks, start=1):
            status = "✔" if task["completed"] else "✘"
            print(f"{index}. [{status}] {task['title']}")

    def mark_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            self.save_tasks()
            print("✅ Task marked as completed!")
        else:
            print("❌ Invalid task number!")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            deleted = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(f"🗑 Deleted task: {deleted['title']}")
        else:
            print("❌ Invalid task number!")


def main():
    todo = TodoList()

    while True:
        print("\n====== TO-DO LIST MENU ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            todo.add_task(title)

        elif choice == "2":
            todo.view_tasks()

        elif choice == "3":
            todo.view_tasks()
            try:
                number = int(input("Enter task number to mark as completed: "))
                todo.mark_completed(number)
            except ValueError:
                print("❌ Please enter a valid number!")

        elif choice == "4":
            todo.view_tasks()
            try:
                number = int(input("Enter task number to delete: "))
                todo.delete_task(number)
            except ValueError:
                print("❌ Please enter a valid number!")

        elif choice == "5":
            print("👋 Exiting To-Do List. Goodbye!")
            break

        else:
            print("❌ Invalid choice! Please select between 1-5.")


if __name__ == "__main__":
    main()
