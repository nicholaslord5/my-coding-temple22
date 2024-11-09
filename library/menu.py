from library.book import Book
from library.user import User
from library.author import Author

books = []
users = []
authors = []

def main_menu():
    while True:
        print("\nWelcome to the Library Management System\nMain Menu:\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            book_menu()
        elif choice == '2':
            user_menu()
        elif choice == '3':
            author_menu()
        elif choice == '4':
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def book_menu():
    print("\nBook Operations:")
    while True:
        print("1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books\n6. Go Back")
        choice = input("Enter your choice: ")
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            genre = input("Enter genre: ")
            pub_date = input("Enter publication date: ")
            book = Book(title, author, genre, pub_date)
            books.append(book)
            print(f"Book '{title}' added successfully!")
        elif choice == '2':
            title = input("Enter the title of the book to borrow: ")
            for book in books:
                if book.get_title() == title and book.borrow():
                    print(f"You have borrowed '{title}'.")
                    break
            else:
                print("Book not available.")
        elif choice == '3':
            title = input("Enter the title of the book to return: ")
            for book in books:
                if book.get_title() == title:
                    book.return_book()
                    print(f"You have returned '{title}'.")
                    break
            else:
                print("Book not found.")
        elif choice == '4':
            title = input("Enter the title to search for: ")
            for book in books:
                if book.get_title() == title:
                    print("Book found:", book.get_details())
                    break
            else:
                print("Book not found.")
        elif choice == '5':
            print("\nList of all books:")
            for book in books:
                print(book.get_details())
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please select a valid option.")

def user_menu():
    print("\nUser Operations:")
    while True:
        print("1. Add a new user\n2. View user details\n3. Display all users\n4. Go Back")
        choice = input("Enter your choice: ")
        if choice == '1':
            user_name = input("Enter user name: ")
            library_id = input("Enter library ID: ")
            user = User(user_name, library_id)
            users.append(user)
            print(f"User '{user_name}' added successfully!")
        elif choice == '2':
            library_id = input("Enter library ID to view details: ")
            for user in users:
                if user.get_library_ID() == library_id:
                    print(f"User: {user.get_user_name()}, Borrowed Books: {user.get_borrowed_books()}")
                    break
            else:
                print("User not found.")
        elif choice == '3':
            print("\nList of all users:")
            for user in users:
                print(f"User: {user.get_user_name()}, Library ID: {user.get_library_ID()}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")

def author_menu():
    print("\nAuthor Operations:")
    while True:
        print("1. Add a new author\n2. View author details\n3. Display all authors\n4. Go Back")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter author name: ")
            biography = input("Enter author biography: ")
            author = Author(name, biography)
            authors.append(author)
            print(f"Author '{name}' added successfully!")
        elif choice == '2':
            name = input("Enter the author's name to view details: ")
            for author in authors:
                if author.get_name() == name:
                    print(f"Author: {author.get_name()}, Biography: {author.get_biography()}")
                    break
            else:
                print("Author not found.")
        elif choice == '3':
            print("\nList of all authors:")
            for author in authors:
                print(f"Author: {author.get_name()}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")
