# Create Operation in Django Shell
## Purpose
This document describes the process for creating a new instance of the Book model using the Django shell.
```
from bookshelf.models import Book 

new_book = Book.objects.create(title = "1984",author = "George Orwell" , publication_year= '1949' )
new_book.save()

# Expected output: <Book: Book object (1)> or similar depending on the primary key
new_book
```