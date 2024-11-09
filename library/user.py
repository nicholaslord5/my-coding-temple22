class User:
    def __init__(self, user_name, library_ID):
        self.__user_name = user_name
        self.__library_ID = library_ID
        self.__borrowed_books = []

    def get_user_name(self):
        return self.__user_name

    def get_library_ID(self):
        return self.__library_ID

    def borrow_book(self, book_title):
        self.__borrowed_books.append(book_title)

    def return_book(self, book_title):
        if book_title in self.__borrowed_books:
            self.__borrowed_books.remove(book_title)

    def get_borrowed_books(self):
        return self.__borrowed_books
