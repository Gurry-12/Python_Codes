'''
Library management system
1. Add a book
2. Display all books
3. Lend a book
4. Return a book
5. Exit
'''

#class Book

class Book:
    
    #constructor 
    def __init__(self, title, author, isbn, total_copies, available_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.available_copies = available_copies
        
    #display book details
    def display(self):
        print('Title:', self.title)
        print('Author:', self.author)
        print('ISBN:', self.isbn)
        print('Total copies:', self.total_copies)
        print('Available copies:', self.available_copies)
        print()
    
    #lend a book
    def lend_book(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            print('Book lent successfully')
        else:
            print('Book not available')
    
    #return a book
    def return_book(self):
        self.available_copies += 1
        print('Book returned successfully')
        
#member class

class Member:
    
    def __init__(self, name, member_id ):
        self.name = name
        self.member_id = member_id
        self.borrowed_copies = [] 
        
    def display(self):
        print('Name:', self.name)
        print('Member ID:', self.member_id)
        print('Borrowed copies are : ')
        for copies in self.borrowed_copies:
            print(copies.title)
        print()
    
    def borrow_book(self, book):
        if book.available_copies > 0:
            book.lend_book()
            self.borrowed_copies.append(book)
            print(f"{self.name} has borrowed the book '{book.title}'.")
        else:
            print("Book not available for borrowing.")
            
    def return_book(self, book):
        if book in self.borrowed_copies:
            book.return_book()
            self.borrowed_copies.remove(book)
            print(f"{self.name} has returned the book '{book.title}'.")
        else:
            print("This book was not borrowed by the member.")
        

# Library class
class Library:
    
    def __init__(self):
        self.book = []
        self.member = []
        
    
    def add_book(self, book):
        self.book.append(book)
        print(f"Book '{book.title}' added to the library.")
        
    def display_books(self):
        for book in self.book:
            book.display()            
            
    def remove_book(self, book):
        if book in self.book:
            self.book.remove(book)
            print(f"Book '{book.title}' removed from the library.")
        else:
            print("Book not found.")
        
    def add_member(self, member):
        self.member.append(member)
        print(f"Member '{member.name}' added to the library.")
        
        
    def remove_member(self, member):
        if member in self.member:
            self.member.remove(member)
            print(f"Member '{member.name}' removed from the library.")
        else:
            print("Member not found.")
        
    def lend_book(self, book, member):
        if book in self.book and member in self.member :
            member.borrow_book(book)
        else:
            print("Book or member not found in the library.")

            
    def return_book(self, book, member):
        if book in self.book and member in self.member:
            member.return_book(book)
        else:
            print("Book or member not found in the library.")

            
    def display_members(self):  
        for member in self.member:
            member.display()
            
#main function

book1 = Book( "Introduction to Algorithms" , "Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein" ," 978-0262033848", 5, 5)
book2 = Book("Artificial Intelligence: A Modern Approach", " Stuart Russell, Peter Norvig", " 978-0136042594 ",4, 4)
book3 = Book("Clean Code: A Handbook of Agile Software Craftsmanship", " Robert C. Martin" , " 978-0132350884 ",6,6)
book4 = Book("Design Patterns: Elements of Reusable Object-Oriented Software", " Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides" ," 978-0201633610 ",7,7)
book5 = Book("Computer Networking: A Top-Down Approach", " James F. Kurose, Keith W. Ross " , "978-0133594140",3,3)
book6 = Book("The Pragmatic Programmer: Your Journey to Mastery", "Andrew Hunt, David Thomas",  "978-0135957059",2,2)
book7 = Book("Database System Concepts", " Abraham Silberschatz, Henry F. Korth, S. Sudarshan ", " 978-0078022159 ",6,6 )
book8 = Book("Operating System Concepts" , " Abraham Silberschatz, Peter B. Galvin, Greg Gagne" , " 978-1118063330 ",5,5)
book9 = Book("Computer Organization and Design: The Hardware/Software Interface"," David A. Patterson, John L. Hennessy" , " 978-0124077263 ",4,4)
book10 = Book("Software Engineering: A Practitioner's Approach", " Roger S. Pressman" , " 978-0078022128",5,5)


member1 = Member("Ram ", 101)
member2 = Member("Ramesh", 102)
member3 = Member("Mohan", 103)

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)
library.add_book(book6)
library.add_book(book7)
library.add_book(book8)
library.add_book(book9)
library.add_book(book10)

library.add_member(member1)
library.add_member(member2)
library.add_member(member3)

    
library.lend_book(book1, member1)

book1.display()
member1.display()

library.return_book(book1, member1)

book1.display()
member1.display()