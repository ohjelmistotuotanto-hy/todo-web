from models.todo import Todo
from repositories.todo_repository import todo_repository as default_todo_repository


class TodoService:
    def __init__(self, todo_repository=default_todo_repository):
        self._todo_repository = todo_repository

    def create_todo(self, content, done=False):
        return self._todo_repository.create(Todo(content=content, done=done))

    def get_all_todos(self):
        return self._todo_repository.find_all()

    def delete_todo(self, todo_id):
        return self._todo_repository.delete_by_id(todo_id)

    def delete_all_todos(self):
        return self._todo_repository.delete_all()

todo_service = TodoService()
