from abc import ABC, abstractmethod


class RequestSource(ABC):

    @abstractmethod
    def exists(self, student_id, topic):
        pass

    @abstractmethod
    def save(self, request):
        pass
