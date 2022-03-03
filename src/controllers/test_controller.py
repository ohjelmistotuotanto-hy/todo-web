from flask import Blueprint
from services.todo_service import todo_service

test_controller = Blueprint("test", __name__)


@test_controller.route("/tests/reset", methods=["POST"])
def reset():
    todo_service.delete_all_todos()

    return "ok"
