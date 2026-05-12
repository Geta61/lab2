from src.domain.request_service import RequestService


class FakeRequestSource:

    def exists(self, student_id, topic):
        return False

    def save(self, request):
        return 10


def test_success_request():
    service = RequestService(FakeRequestSource())

    result = service.process(
        1,
        "schedule",
        "Need help"
    )

    assert result == "Request created #10"
