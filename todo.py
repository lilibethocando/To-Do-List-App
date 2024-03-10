import csv

class Task:
    def __init__(self, description):
        self.unique_id = None
        self.description = description
        self.completed = False

    def __str__(self) -> str:
        return f"Task ID: {self.unique_id}\n Description: {self.description}\n Completed: {self.completed}"

    def __repr__(self) -> str:
        return f"<Task:{self.unique_id}>"

class TodoList:
    def __init__(self):
        self.tasks = {}
        self.unique_id = 1

    def add_task(self, description):
        task = Task(description)
        task.unique_id = self.unique_id
        self.unique_id += 1
        self.tasks[task.unique_id] = task
        return task

    def edit_task(self, task_id, new_description):
        task = self.tasks.get(task_id)
        if task:
            task.description = new_description
            return True
        else:
            print("Warning", "Task not found.")
            return False

    def search_task(self, id):
        return self.tasks.get(id)

    def show_tasks(self):
        for task_id, task in self.tasks.items():
            print(task)

    def remove_task(self, id):
        if id in self.tasks:
            del self.tasks[id]
        else:
            print("Task not found")

    def mark_completed(self, id):
        task = self.tasks.get(id)
        if task:
            task.completed = True
        else:
            print("Task not found")

    def create_file(self):
        headers = ["ID", "Description", "Completed"]
        with open("tasks.txt", "w", newline= '') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for task_id, task in self.tasks.items():
                writer.writerow({"ID": task_id, "Description": task.description, "Completed": task.completed})
        return file
        
