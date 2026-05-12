from src.infrastructure.request_source_factory import RequestSourceFactory
from src.domain.request_service import RequestService


source = RequestSourceFactory.create()

service = RequestService(source)

result = service.process(
    1001,
    "schedule",
    "Need consultation"
)

print(result)
