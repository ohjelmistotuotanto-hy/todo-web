from models.todo import Todo
from app import db


class TodoRepository:
    def find_all(self):
        return Todo.query.all()

    def create(self, todo):
        db.session.add(todo)
        db.session.commit()

        return todo
    
    def delete_all(self):
        return Todo.query.delete()


todo_repository = TodoRepository()
