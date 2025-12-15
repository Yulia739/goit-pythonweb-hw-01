import logging
from interfaces.LibraryInterface import LibraryInterface
from models.book import Book

logger = logging.getLogger(__name__)

class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        books = self.library.get_books()
        if not books:
            logger.info("Library is empty")
            return
        for book in books:
            logger.info(f'Title: {book.title}, Author: {book.author}, Year: {book.year}')
