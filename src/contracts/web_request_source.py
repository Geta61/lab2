from src.contracts.request_source import RequestSource


class WebServiceRequestSource(RequestSource):

    def exists(self, student_id, topic):
        print("HTTP GET /requests")
        return False

    def save(self, request):
        print("HTTP POST /requests")
        return 501
