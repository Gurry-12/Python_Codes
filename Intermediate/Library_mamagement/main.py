# ### Library Management System Mini Project

# #### Problem Statement

# Design a Library Management System using Object-Oriented Programming (OOP) principles in Python.
# The system should manage books, library members, and book loans, incorporating appropriate classes,
# attributes, and methods to facilitate interactions.

# #### Requirements

# 1. **Class Design:**

#    - **Book:**
#      - **Attributes:**
#        - `title`: The title of the book.
#        - `author`: The author of the book.
#        - `isbn`: The unique identifier for the book.
#        - `total_copies`: The total number of copies available in the library.
#        - `available_copies`: The number of copies currently available for borrowing.
#      - **Methods:**
#        - `display_info()`: Display information about the book.
#        - `lend_book()`: Lend a book if copies are available, reducing the count of `available_copies`.
#        - `return_book()`: Return a book, increasing the count of `available_copies`.

#class 1
class Book:
    def __init__(self, title, author, isbn, total_copies, available_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.available_copies = available_copies


    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Total Copies: {self.total_copies}")
        print(f"Available Copies: {self.available_copies}")

    def lend_book(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            print("Book lent successfully!")
        else:
            print("Book not available for lending.")

    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            print("Book returned successfully!")
        else:
            print("No copies of this book are currently lent out.")

#    - **Member:**
#      - **Attributes:**
#        - `name`: The name of the member.
#        - `member_id`: The unique identifier for the member.
#        - `borrowed_books`: A list of `Book` objects borrowed by the member.
#      - **Methods:**
#        - `borrow_book(book)`: Borrow a book, adding it to `borrowed_books` and reducing the `available_copies` of the book.
#        - `return_book(book)`: Return a book, removing it from `borrowed_books` and increasing the `available_copies` of the book.
#        - `display_info()`: Display information about the member, including borrowed books.
            
#class 2
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available_copies > 0:
            book.lend_book()
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed the book '{book.title}'.")
        else:
            print("Book not available for borrowing.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned the book '{book.title}'.")
        else:
            print("This book was not borrowed by the member.")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Member ID: {self.member_id}")
        print("Borrowed Books:")
        for book in self.borrowed_books:
            print(f"- {book.title}")
            

#    - **Library:**
#      - **Attributes:**
#        - `books`: A list of `Book` objects in the library.
#        - `members`: A list of `Member` objects registered with the library.
#      - **Methods:**
#        - `add_book(book)`: Add a new book to the library.
#        - `remove_book(book)`: Remove a book from the library.
#        - `add_member(member)`: Register a new member to the library.
#        - `remove_member(member)`: Deregister a member from the library.
#        - `lend_book(book, member)`: Lend a book to a member, updating the `available_copies` of the book and the member's `borrowed_books`.
#        - `return_book(book, member)`: Process the return of a book from a member, updating the `available_copies` of the book and the member's `borrowed_books`.
#        - `display_books()`: Display a list of all books in the library.
#        - `display_members()`: Display a list of all members registered with the library.

#class 3 
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book.title}' removed from the library.")
        else:
            print("Book not found in the library.")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' added to the library.")

    def remove_member(self, member):
        if member in self.members:
            self.members.remove(member)
            print(f"Member '{member.name}' removed from the library.")
        else:
            print("Member not found in the library.")

    def lend_book(self, book, member):
        if book in self.books and member in self.members:
            member.borrow_book(book)
        else:
            print("Book or member not found in the library.")

    def return_book(self, book, member):
        if book in self.books and member in self.members:
            member.return_book(book)
        else:
            print("Book or member not found in the library.")

    def display_books(self):
        print("Books in the Library:")
        for book in self.books:
            print(f"- {book.title}")

    def display_members(self):
        print("Members of the Library:")
        for member in self.members:
            print(f"- {member.name}")
            


# 2. **Interactions:**

#    - The library should be able to add and remove books.
#    - Members should be able to register and deregister.
#    - Members should be able to borrow and return books.
#    - The system should keep track of the available copies of each book.
#    - The system should handle edge cases such as attempting to borrow a book that is not available or attempting to return a book that was not borrowed.

# 3. **Additional Features (Optional):**

#    - Search for books by title or author.
#    - Display the list of books borrowed by a particular member.
#    - Implementing properties with getters and setters for attributes where appropriate.

# #### Example Usage

# Here is an example of how the Library Management System could be used:


# Create some book objects
book1 = Book("Python Programming", "John Doe", "123456", 5, 5)
book2 = Book("Java Programming", "Jane Smith", "654321", 3, 3)
book3 = Book("Web Development", "Alice Johnson", "987654", 2, 2)

# Create some member objects
member1 = Member("Alice", "M001")
member2 = Member("Bob", "M002")

# Create a library object
library = Library()

# Add books to the library
library.add_book(book1)

# Add members to the library
library.add_member(member1)

# Display the list of books in the library
library.display_books()

# Display the list of members in the library
library.display_members()

# Lend a book to a member
library.lend_book(book1, member1)

# Display the list of books borrowed by a member
member1.display_info()

# Return a book from a member
library.return_book(book1, member1)

# Remove a book from the library
library.remove_book(book1)

# Remove a member from the library
library.remove_member(member1)


# #### Detailed Question

# Design and implement the following classes and methods for a Library Management System in Python:

# 1. **Book Class:**
#    - Define the attributes `title`, `author`, `isbn`, `total_copies`, and `available_copies`.
#    - Implement methods to display book information, lend a book, and return a book.

# 2. **Member Class:**
#    - Define the attributes `name`, `member_id`, and `borrowed_books`.
#    - Implement methods to borrow a book, return a book, and display member information.

# 3. **Library Class:**
#    - Define the attributes `books` and `members`.
#    - Implement methods to add and remove books, add and remove members, lend a book to a member, return a book from a member, and display lists of books and members.

# 4. **Interactions:**
#    - Ensure that the library can add and remove books.
#    - Ensure that members can register and deregister.
#    - Ensure that members can borrow and return books, with the system tracking the number of available copies of each book.
#    - Handle edge cases such as borrowing a book that is not available and returning a book that was not borrowed.

# 5. **Optional Features:**
#    - Implement a search functionality for books by title or author.
#    - Display the list of books borrowed by a particular member.
#    - Use properties with getters and setters where appropriate to manage attribute access.

# By completing this project, you will demonstrate an understanding of OOP principles such as encapsulation, 
# inheritance, and polymorphism, and you will gain practical experience in designing and implementing a real-world application using Python.



