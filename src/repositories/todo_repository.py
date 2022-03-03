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
        result = Todo.query.delete()
        db.session.commit()

        return result

    def delete_by_id(self, todo_id):
        result = Todo.query.filter(Todo.id == todo_id).delete()
        db.session.commit()

        return result


todo_repository = TodoRepository()
