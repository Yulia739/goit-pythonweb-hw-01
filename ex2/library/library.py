from typing import List
import logging

from interfaces.LibraryInterface import LibraryInterface
from models.book import Book


logger = logging.getLogger(__name__)

class Library(LibraryInterface):
    def __init__(self) -> None:
        self._books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)
        logger.info(f'Book added: {book.title} by {book.author} ({book.year})')

    def remove_book(self, title: str) -> None:
        for book in self._books:
            if book.title == title:
                self._books.remove(book)
                logger.info(f'Book removed: {title}')
                break

    def get_books(self) -> List[Book]:
        return self._books.copy()
