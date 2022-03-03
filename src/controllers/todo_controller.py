from flask import render_template, Blueprint, request, redirect
from services.todo_service import todo_service

todo_controller = Blueprint("todo", __name__)


@todo_controller.route("/")
def get_all_todos():
    todos = todo_service.get_all_todos()

    return render_template("todo-list.html", todos=todos, todos_count=len(todos))


@todo_controller.route("/todos", methods=["POST"])
def create_todo():
    content = request.form.get("content")

    todo_service.create_todo(content)

    return redirect("/")


@todo_controller.route("/todos/delete/<todo_id>", methods=["POST"])
def delete_todo(todo_id):
    todo_service.delete_todo(int(todo_id))

    return redirect("/")
