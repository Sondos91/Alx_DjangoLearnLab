from django.urls import path
from . import views

urlpatterns = [
    # Add URL patterns for your views here
    # For example:
    path('authors/', views.AuthorListView.as_view()),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view()),
    path('books/', views.BookListView.as_view()),
    path('books/<int:pk>/', views.BookDetailView.as_view()),
]

urlpatterns = [
    path('books/', views.BookListView.as_view()),
    path("booksdetail", views.BookDetailView.as_view()),
    path("books/create",views.BookCreateView.as_view()),
    path("books/update", views.BookUpdateView.as_view()),
    path("books/delete", views.BookDeleteView.as_view()),
]
