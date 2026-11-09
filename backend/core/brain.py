from datetime import datetime

from backend.memory.store import memory


class ItachiCore:

    def __init__(self):
        self.name = "PROJECT ITACHI 2.0"
        self.status = "ONLINE"
        self.version = "2.0.0"

    def get_status(self):
        return {
            "name": self.name,
            "status": self.status,
            "version": self.version,
            "time": datetime.now().isoformat()
        }

    def think(self, task: str):
        return {
            "agent": self.name,
            "task": task,
            "status": "RECEIVED",
            "message": "Task received. Preparing analysis."
        }

    def remember(self, category: str, content: str):
        return memory.save(category, content)

    def recall(self, limit: int = 20):
        return memory.get_recent(limit)

    def search_memory(self, keyword: str):
        return memory.search(keyword)


itachi = ItachiCore()