from django.shortcuts import render ,get_object_or_404, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from .models import Library
from .models import Book 
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from .forms import BookForm 

def list_books(request):
    books = Book.objects.all() 
    context = {'book_list': books} 
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        context['book'] = self.object.books.all()
        return context


class register(CreateView):
    form_class = UserCreationForm() 
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'
    
    

def is_admin(user):
    return user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    # This view is only accessible to users with the 'Admin' role
    return render(request, 'relationship_app/admin_view.html')  # You can customize the template as needed

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    # This view is only accessible to users with the 'Librarian' role
    return render(request, 'relationship_app/librarian_view.html') 

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    # This view is only accessible to users with the 'Member' role
    return render(request, 'relationship_app/member_view.html')  



@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Replace 'book_list' with the appropriate view name
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

# View to edit a book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Replace 'book_list' with the appropriate view name
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})

# View to delete a book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Replace 'book_list' with the appropriate view name
    return render(request, 'relationship_app/delete_book.html', {'book': book})