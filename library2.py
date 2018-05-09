from collections import namedtuple

class Library(object):
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def book_with_ISBN(self, ISBN):
        for book in self.books:
            if book.ISBN == ISBN:
                return book

    def books_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def books_under_price(self, price):
        return [book for book in self.books if book.price < price]


Book = namedtuple('Book', 'name author ISBN price')

library = Library()
library.add_book(Book('Geometry', 'Jeff Potter', '0596805888', 22))
library.add_book(Book('Math', 'George Harr', '0594805888', 15))
library.add_book(Book('English', 'James Odd', '0596225888', 10))
library.add_book(Book('Physics', 'Jeff Potter', '0597884512', 18))
print(library.book_with_ISBN('0594805888'))
print(library.books_by_author('George Harr'))
print(library.books_under_price(20))
