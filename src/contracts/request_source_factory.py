import json

from src.infrastructure.db_request_source import DatabaseRequestSource
from src.infrastructure.file_request_source import FileRequestSource
from src.infrastructure.web_request_source import WebServiceRequestSource


class RequestSourceFactory:

    @staticmethod
    def create(config_path="config.json"):

        with open(config_path) as f:
            config = json.load(f)

        source_type = config["dataSourceType"]

        if source_type == "db":
            return DatabaseRequestSource()

        if source_type == "file":
            return FileRequestSource()

        if source_type == "web":
            return WebServiceRequestSource()

        raise ValueError("Unknown data source type")
