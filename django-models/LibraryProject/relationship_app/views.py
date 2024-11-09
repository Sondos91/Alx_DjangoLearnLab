from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book , Library

def book_list(request):      
      books = Book.objects.all()  
      context = {'book_list': books} 
      return render(request, 'templates/list_books.html', context)

class LibraryDetailView(DetailView):
      model = Library
      template_name = 'templates/library_detail.html'
      context_object_name = 'library'
      
      def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        book = self.get_object()  
        context['book'] = self.object.books.all()
        return context
      