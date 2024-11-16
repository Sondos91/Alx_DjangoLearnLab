# Delete Operation in Django Shell
## Purpose
This document describes the process for deleting an instance of the Book model using the Django shell. In this example, we will delete the book titled "1984" and confirm the deletion by retrieving all Book instances from the database.
```
# Import the Book model
from bookshelf.models import Book

# Retrieve the book to be deleted
book = Book.objects.get(title='1984')

book.delete()
# Expected output: (1, {'library.Book': 1}), indicating one `Book` instance was deleted

# Confirm deletion by retrieving all books

all_books = Book.objects.all()
all_books  # Expected Output: <QuerySet []> if no other books exist, or a list of remaining books
```