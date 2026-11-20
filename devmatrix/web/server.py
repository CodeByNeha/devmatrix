import http.server
import urllib.parse
from pathlib import Path
from ..api.router import Router
from ..api.response import Response

STATIC_DIR = Path(__file__).parent / "static"
TEMPLATE_DIR = Path(__file__).parent / "templates"

class DevMatrixHttpHandler(http.server.BaseHTTPRequestHandler):
    router = None

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/":
            html = (TEMPLATE_DIR / "index.html").read_text(encoding="utf-8")
            self._send_response(*Response.html(html))
            return

        if path.startswith("/static/"):
            file_name = path.replace("/static/", "")
            target = STATIC_DIR / file_name
            if target.exists():
                ctype = "text/css" if file_name.endswith(".css") else "application/javascript"
                self._send_response(200, ctype, target.read_bytes())
                return

        handler, params = self.router.dispatch("GET", path)
        if handler:
            self._send_response(*handler(params, b""))
        else:
            self._send_response(*Response.error("Endpoint not found", status=404))

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)
        parsed = urllib.parse.urlparse(self.path)
        handler, params = self.router.dispatch("POST", parsed.path)
        if handler:
            self._send_response(*handler(params, body))
        else:
            self._send_response(*Response.error("Endpoint not found", status=404))

    def _send_response(self, status, content_type, body):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        pass
