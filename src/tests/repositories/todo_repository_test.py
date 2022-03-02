import unittest
from repositories.todo_repository import todo_repository
from models.todo import Todo


class TestTodoRepository(unittest.TestCase):
    def setUp(self):
        todo_repository.delete_all()

    def test_create(self):
        todo_repository.create(Todo(content="learn python", done=False))
        todos = todo_repository.find_all()

        self.assertEqual(len(todos), 1)
        self.assertEqual(todos[0].content, "learn python")
