from models import Author, Book, Library, Librarian

author = Author.objects.get(name= "George Orwell")

books = Book.objects.all()

librarian = Librarian.objects.get(Library= "Animal Farm")

