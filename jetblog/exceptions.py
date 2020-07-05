class APIError(Exception):
    def __init__(self, code=500, message="Server Error", errors=[]):
        self.code = code
        self.message = message
        self.errors = errors

    @property
    def response(self):
        json = {"error": {
            "code": self.code,
            "message": self.message,
        }}

        if self.errors:
            json.update({"errors": self.errors})

        return json
