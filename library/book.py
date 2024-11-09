class Book:
    def __init__(self, title, author, genre, publication_date, availability=True):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__availability = availability

    def get_title(self):
        return self.__title

    def is_available(self):
        return self.__availability

    def borrow(self):
        if self.__availability:
            self.__availability = False
            return True
        return False

    def return_book(self):
        self.__availability = True

    def get_details(self):
        return (f"Title: {self.__title}, Author: {self.__author}, Genre: {self.__genre}, "
                f"Publication Date: {self.__publication_date}, Available: {self.__availability}")
