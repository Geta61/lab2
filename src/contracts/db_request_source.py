from src.contracts.request_source import RequestSource


class DatabaseRequestSource(RequestSource):

    def exists(self, student_id, topic):
        print("DB query")
        return False

    def save(self, request):
        print("DB insert")
        return 101
