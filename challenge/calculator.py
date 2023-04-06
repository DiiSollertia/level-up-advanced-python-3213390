class Calculator:
    def __init__(self, *args: Exception):
        self.error = None
        self.exc_types = args

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.error = exc_value
        return isinstance(exc_value, self.exc_types)
