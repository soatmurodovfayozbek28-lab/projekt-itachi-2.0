import unittest
from uuid import uuid4
from fastapi.testclient import TestClient

from backend.api.main import app

client = TestClient(app)


class ItachiAPITests(unittest.TestCase):

    def test_home(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_status(self):
        response = client.get("/status")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ONLINE")

    def test_think(self):
        response = client.post(
            "/think",
            json={"task": "Analyze my goals"}
        )
        self.assertEqual(response.status_code, 200)

    def test_memory(self):
        content = f"Test memory {uuid4()}"

        response = client.post(
            "/memory",
            json={
                "category": "test",
                "content": content
            }
        )
        self.assertEqual(response.status_code, 200)

        search = client.get(
            "/memory/search",
            params={"keyword": content}
        )
        self.assertEqual(search.status_code, 200)
        self.assertTrue(len(search.json()) > 0)


if __name__ == "__main__":
    unittest.main()