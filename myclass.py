class Book:
    # Represents a book with basic attributes and functionalities.
    def __init__(self, title, author, isbn, pages):
        # Constructor to initialize a Book object.
        self.title = title
        self.author = author
        self.isbn = isbn
        self.pages = pages
        self.current_page = 1

    def read_page(self, page_number):
        # Reads a specific page in the book.
        if 1 <= page_number <= self.pages:
            self.current_page = page_number
            print(f"Reading page {self.current_page} of '{self.title}'.")
        else:
            print(f"Invalid page number.  '{self.title}' has {self.pages} pages.")

    def __str__(self):
        # Returns a string representation of the Book object.
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Pages: {self.pages}, Current Page: {self.current_page}"

class EBook(Book):
    # Represents an electronic book, inheriting from the Book class.
    def __init__(self, title, author, isbn, pages, file_format, file_size_mb):
        # Constructor to initialize an EBook object.
        super().__init__(title, author, isbn, pages)
        self.file_format = file_format
        self.file_size_mb = file_size_mb

    def display_info(self):
        # Displays information about the EBook, including format and size.
        print(f"{super().__str__()}, File Format: {self.file_format}, File Size: {self.file_size_mb} MB")

    def __str__(self):
        # Returns a string representation of the EBook object.
        return f"{super().__str__()}, File Format: {self.file_format}, File Size: {self.file_size_mb} MB"


# Create instances of Book and EBook
book1 = Book("The Lord of the Rings", "J.R.R. Tolkien", "978-0547928227", 1178)
ebook1 = EBook("Pride and Prejudice", "Jane Austen", "978-0141439518", 432, "EPUB", 1.2)

# Demonstrate the methods
print(book1)
book1.read_page(50)

print("\n" + str(ebook1))
ebook1.read_page(100)
ebook1.display_info()
