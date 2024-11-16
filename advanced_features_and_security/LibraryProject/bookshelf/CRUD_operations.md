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
```quit
