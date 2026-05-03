from app.books import Book
from app.interfaces import PrintBookInterface


class PrintBook(PrintBookInterface):
    def __init__(self, book: Book):
        self.book = book

    def print_book(self):
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)


class PrintReversedBook(PrintBook):
    def __init__(self, book: Book):
        super().__init__(book=book)

    def print_book(self):
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])
