from src.contracts.request_source import RequestSource


class FileRequestSource(RequestSource):

    def __init__(self):
        self.storage = []

    def exists(self, student_id, topic):
        return any(
            r["student_id"] == student_id and r["topic"] == topic
            for r in self.storage
        )

    def save(self, request):
        self.storage.append(request)
        return len(self.storage)
