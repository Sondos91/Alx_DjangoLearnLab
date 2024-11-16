# Update Operation in Django Shell
## Purpose
This document describes the process for updating an existing Book instance in the Django shell. In this example, we will change the title of the book titled "1984" to "Nineteen Eighty-Four" and save the changes.
```
from library.models import Book

# Retrieve the book by title
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()  # Save the changes to the database

# Expected output: 'Nineteen Eighty-Four', confirming the title has been updated
book.title # Output: 'Nineteen Eighty-Four'
```