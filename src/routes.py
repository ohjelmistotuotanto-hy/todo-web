from flask import (
    render_template,
)

from app import app
from services.todo_service import todo_service


@app.route("/")
def render_counter():
    todos = todo_service.get_all_todos()

    print(todos)

    return render_template("todo-list.html")
