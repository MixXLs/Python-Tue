class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return f"'{self.title}' has been checked out."
        else:
            return f"'{self.title}' is already checked out."

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return f"'{self.title}' has been returned."
        else:
            return f"'{self.title}' was not checked out."


# Creating book objects
book1 = Book("1984", "George Orwell", "1234567890")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")

# Checking out and returning books
print(book1.check_out())   # Output: '1984' has been checked out.
print(book1.return_book()) # Output: '1984' has been returned.
print(book2.check_out())   # Output: 'To Kill a Mockingbird' has been checked out.
