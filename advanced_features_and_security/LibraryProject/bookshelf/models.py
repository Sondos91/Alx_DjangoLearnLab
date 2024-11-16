from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import Group, Permission

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

   
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, date_of_birth=None, profile_photo=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            profile_photo=profile_photo,   
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, date_of_birth=None, profile_photo=None):
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
            profile_photo=profile_photo,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
    class Meta:
        permissions = [
            ("can_view", "view_user"),
            ("can_create", "create_user"),
            ("can_edit", "edit_user"),
            ("can_delete", "delete_user"),
        ]
 
    
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()
    is_admin = models.BooleanField(default=False)
    objects = CustomUserManager()
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'profile_photo']

editors_group, created = Group.objects.get_or_create(name='Editors')
viewers_group, created = Group.objects.get_or_create(name='Viewers')
admins_group, created = Group.objects.get_or_create(name='Admins')
can_edit_permission = Permission.objects.get(codename='can_edit')
can_create_permission = Permission.objects.get(codename='can_create')
can_view_permission = Permission.objects.get(codename='can_view')
can_delete_permission = Permission.objects.get(codename='can_delete')

editors_group.permissions.add(can_edit_permission, can_create_permission)
viewers_group.permissions.add(can_view_permission)
admins_group.permissions.add(can_edit_permission, can_create_permission, can_view_permission, can_delete_permission)