# 4. Problem: ToDo List 
# Description: Create a ToDo class with methods to add tasks, mark tasks as completed, and 
# display the list of tasks.

class ToDo:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
    def mark_as_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
        else:
            print("Invalid task index.")
    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for index, task_info in enumerate(self.tasks):
                status = " [x] " if task_info["completed"] else " [ ] "
                print(f"{index + 1}.{status} {task_info['task']}")

# Example usage:
todo_list = ToDo()

todo_list.add_task("Buy groceries")
todo_list.add_task("Complete homework")
todo_list.add_task("Go for a run")

todo_list.display_tasks()

todo_list.mark_as_completed(1)
todo_list.display_tasks()