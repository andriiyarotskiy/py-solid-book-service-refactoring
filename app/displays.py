from app.books import Book
from app.interfaces import DisplayBookInterface


class DisplayBook(DisplayBookInterface):
    def __init__(self, book: Book):
        self.book = book

    def display(self):
        print(self.book.content)


class DisplayReversedBook(DisplayBook):
    def __init__(self, book: Book):
        super().__init__(book=book)

    def display(self):
        print(self.book.content[::-1])
