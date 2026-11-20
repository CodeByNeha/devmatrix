import re

class Router:
    def __init__(self):
        self.routes = []

    def add(self, method: str, pattern: str, handler):
        regex = "^" + re.sub(r":([a-zA-Z_]+)", r"(?P<>[^/]+)", pattern) + "$"
        self.routes.append((method.upper(), re.compile(regex), handler))

    def dispatch(self, method: str, path: str):
        for m, regex, handler in self.routes:
            if m == method.upper():
                match = regex.match(path)
                if match:
                    return handler, match.groupdict()
        return None, None
