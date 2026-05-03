from app.interfaces import BookInterface


class Book(BookInterface):
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content
