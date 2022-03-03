from flask import render_template, Blueprint
from services.todo_service import todo_service

todos_controller = Blueprint("todos", __name__)


@todos_controller.route("/")
def get_all_todos():
    todos = todo_service.get_all_todos()

    return render_template("todo-list.html", todos=todos)
