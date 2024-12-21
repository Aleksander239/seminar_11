from utils.file_handler import FileHandler
from models.task import Task

class TaskService:
    def __init__(self, file_path='data/tasks.json'):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        file_handler = FileHandler(self.file_path)
        tasks_data = file_handler.read_json_file()
        return [Task(**task_data) for task_data in tasks_data]

    def save_tasks(self):
        tasks_data = [task.to_dict() for task in self.tasks]
        file_handler = FileHandler(self.file_path)
        file_handler.write_json_file(tasks_data)

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def get_all_tasks(self):
        return self.tasks

    def find_task(self, id):
        for i in range(len(self.tasks)):
            if id == self.tasks[i].to_dict()['id']:
                return self.tasks[i].to_dict()

    def update_task(self, id, updated_task):
        for i in range(len(self.tasks)):
            if id == self.tasks[i].to_dict()['id']:
                self.tasks[i] = updated_task
                self.save_tasks()

    def delete_task(self, id):
        for i in range(len(self.tasks)):
            if id == self.tasks[i].to_dict()['id']:
                del self.tasks[i]
                self.save_tasks()

    def mark_as_done(self, id):
        for i in range(len(self.tasks)):
            if id == self.tasks[i].to_dict()['id']:
                self.tasks[i].done = True
                self.save_tasks()

    def export_to_csv(self):
        tasks_data = [task.to_dict() for task in self.tasks]
        file_handler = FileHandler('export.csv')
        file_handler.export_to_csv(tasks_data, ['id', 'title', 'description', 'priority', 'due_date', 'done'])

    def import_from_csv(self):
        file_handler = FileHandler('import.csv')
        imported_tasks = file_handler.import_from_csv(['id', 'title', 'description', 'priority', 'due_date', 'done'])
        for task in imported_tasks:
            self.add_task(Task(task['id'], task['title'], task['description'], task['priority'], task['due_date'], task['done']))
