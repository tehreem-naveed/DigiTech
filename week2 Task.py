# task_manager.py

import json
import os


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists('tasks.txt'):
            with open('tasks.txt', 'r') as file:
                self.tasks = json.load(file)

    def save_tasks(self):
        with open('tasks.txt', 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self, title, priority):
        task_id = len(self.tasks) + 1
        task = {"id": task_id, "title": title, "priority": priority, "completed": False}
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for task in self.tasks:
            status = "Complete" if task["completed"] else "Incomplete"
            print(f"{task['id']}: {task['title']} | Priority: {task['priority']} | Status: {status}")

    def update_task(self, task_id, title=None, priority=None):
        for task in self.tasks:
            if task["id"] == task_id:
                if title:
                    task["title"] = title
                if priority:
                    task["priority"] = priority
                return
        print("Task not found.")

    def mark_complete(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                return
        print("Task not found.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                return
        print("Task not found.")

    def filter_tasks(self, status=None, priority=None):
        filtered_tasks = self.tasks
        if status:
            filtered_tasks = [task for task in filtered_tasks if task["completed"] == (status == "complete")]
        if priority:
            filtered_tasks = [task for task in filtered_tasks if task["priority"].lower() == priority.lower()]

        if not filtered_tasks:
            print("No tasks match the filter.")
            return

        for task in filtered_tasks:
            print(
                f"{task['id']}: {task['title']} | Priority: {task['priority']} | Status: {'Complete' if task['completed'] else 'Incomplete'}")


def main():
    manager = TaskManager()
    while True:
        print("===== Task Manager =====")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Mark a task as complete")
        print("5. Delete a task")
        print("6. Filter tasks")
        print("7. Exit")
        choice = input("========================\nEnter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            priority = input("Enter task priority (Low, Medium, High): ")
            manager.add_task(title, priority)
        elif choice == '2':
            manager.view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            title = input("Enter new title (leave blank to keep current): ")
            priority = input("Enter new priority (leave blank to keep current): ")
            manager.update_task(task_id, title if title else None, priority if priority else None)
        elif choice == '4':
            task_id = int(input("Enter task ID to mark as complete: "))
            manager.mark_complete(task_id)
        elif choice == '5':
            task_id = int(input("Enter task ID to delete: "))
            manager.delete_task(task_id)
        elif choice == '6':
            status = input("Filter by status (complete/incomplete): ")
            priority = input("Filter by priority (Low, Medium, High): ")
            manager.filter_tasks(status if status else None, priority if priority else None)
        elif choice == '7':
            manager.save_tasks()
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
