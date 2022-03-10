from flask import Blueprint, request
from services.todo_service import todo_service

test_controller = Blueprint("test", __name__)


@test_controller.route("/tests/reset", methods=["POST"])
def reset():
    todo_service.delete_all_todos()

    return "ok"

@test_controller.route("/tests/todos", methods=["POST"])
def create_todo():
    content = request.json["content"]
    done = request.json["done"]

    todo_service.create_todo(content, done)

    return "ok"
