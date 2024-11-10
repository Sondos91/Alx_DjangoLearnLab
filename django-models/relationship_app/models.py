from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100) 
    
    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
    class Meta:
        permissions = [
            ('can_add_book', 'Can add book'),
            ('can_change_book', 'Can change book'),
            ('can_delete_book', 'Can delete book'),
        ]
    
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    def __str__(self):
        return self.name
    
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    role = models.CharField(max_length=100 , choices=[('Librarian', 'Librarian'), ('Admin', 'Admin'), ('Member', 'Member')])
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)