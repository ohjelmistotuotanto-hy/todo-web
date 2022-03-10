import requests


class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5000"

        self.reset_application()

    def reset_application(self):
        requests.post(f"{self._base_url}/tests/reset")

    def create_todo(self, content, done = "False"):
        done_boolean = True if done == "True" else False

        data = {
            "content": content,
            "done": done_boolean
        }

        requests.post(f"{self._base_url}/tests/todos", json=data)
