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