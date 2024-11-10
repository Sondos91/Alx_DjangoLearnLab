from django.urls import path
from .views import list_books
from .views import LibraryDetailView 
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import register
from . import views

urlpatterns = [
    path('register/', views.register.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('library/', LibraryDetailView.as_view(), name='library-detail'),
    path('list_books/', list_books, name='list_books'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('add/', views.add_book, name='add_book/'),
    path('edit/<int:pk>/', views.edit_book, name='edit_book/'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book/'),
]