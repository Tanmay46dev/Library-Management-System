class Library:
    def __init__(self, name, book_list):
        self.name = name
        self.available_books = book_list
        self.borrowed_books = {}

    def get_available_books(self):
        return self.available_books

    def get_borrowed_books(self):
        return self.borrowed_books

    def get_book_owner(self, book_name):
        return self.get_borrowed_books().get(book_name)

    def is_book_borrowed(self, book_name):
        return book_name in self.borrowed_books.keys()

    def is_book_available(self, book_name):
        return book_name in self.available_books

    def add_book(self, book_name):
        self.available_books.append(book_name)

    def borrow_book(self, book_name, username):
        self.available_books.remove(book_name)
        self.borrowed_books[book_name] = username

    def return_book(self, book_name):
        self.borrowed_books.pop(book_name)
        self.add_book(book_name)

    def remove_book(self, book_name):
        self.available_books.remove(book_name)

