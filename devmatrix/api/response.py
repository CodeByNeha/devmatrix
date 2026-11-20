import json

class Response:
    @staticmethod
    def json(data, status: int = 200) -> tuple:
        body = json.dumps(data)
        return status, "application/json", body.encode("utf-8")

    @staticmethod
    def html(content: str, status: int = 200) -> tuple:
        return status, "text/html; charset=utf-8", content.encode("utf-8")

    @staticmethod
    def error(message: str, status: int = 400) -> tuple:
        return Response.json({"error": message, "status": status}, status=status)
