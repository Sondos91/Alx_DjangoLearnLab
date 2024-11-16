# Retrive Operation in Django Shell
## Purpose
Ensure that the Book instance with the title "1984" already exists in the database.
```
from bookshelf.models import Book
book = Book.objects.get()
book.title # Expected Output: '1984'
book.author # Expected Output: 'George Orwell'
book.publication_year # Expected Output: 1949
```