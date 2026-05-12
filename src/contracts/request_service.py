class RequestService:

    def __init__(self, request_source):
        self.request_source = request_source

    def process(self, student_id, topic, text):

        if not student_id or not topic or not text:
            raise ValueError("Bad request")

        if self.request_source.exists(student_id, topic):
            return "Already exists"

        request = {
            "student_id": student_id,
            "topic": topic,
            "text": text
        }

        request_id = self.request_source.save(request)

        return f"Request created #{request_id}"
