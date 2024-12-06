from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignUpForm, loginForm , ProfileForm , PostForm , CommentForm
from .models import Post , Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy , reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    posts=Post.objects.all()
    context = {'posts': posts }
    return render(request, 'blog/blogs.html', context)

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'blog/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = loginForm()
    return render(request, 'blog/login.html', {'form': form})

def profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = ProfileForm(instance=user)
    return render(request, 'blog/profile.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')  
    return redirect('login')

class CreateView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog')
    
    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class ListView(ListView):
    model = Post
    template_name = 'blog/blogs.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        return Post.objects.all() 
    
class DetailView(DetailView):
    model = Post
    template_name = 'blog/post_details.html'
    context_object_name = 'post'            
    def get_queryset(self):
        return Post.objects.filter(id = self.kwargs['pk'])

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']  # Fields to display in the form
    template_name = 'blog/post_update.html'  # Template for the update form
    success_url = reverse_lazy('blog')  # Redirect to post list after successful update

    def form_valid(self, form):
        """
        Additional logic (if needed) before saving the form.
        """
        form.instance.author = self.request.user  # Ensure the author remains the same
        return super().form_valid(form)

    def test_func(self):
        """
        Restrict access to the original author of the post.
        """
        post = self.get_object()
        return post.author == self.request.user
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'  # Template for confirmation
    success_url = reverse_lazy('blog')  # Redirect to the post list after deletion

    def test_func(self):
        """
        Restrict delete access to the author of the post.
        """
        post = self.get_object()
        return post.author == self.request.user
    
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'
    
    def form_valid(self , form):
        post = get_object_or_404(Post , id = self.kwargs['post_id'])
        form.instance.author = self.request.user
        form.instance.post = post
        return super().form_valid(form)
    
    def get_success_url(self):
        post_id = self.kwargs['post_id']
        return reverse('post_detail' , kwargs = {'post_id':post_id})
    

class CommentListView(ListView):
    model = Comment
    template_name = 'blog/comments.html'
    context_object_name = 'comments'    
    
    def get_queryset(self):
        post = get_object_or_404(Post , id = self.kwargs['post_id'])
        return Comment.objects.filter(post = post)
    
    def get_context_data(self , **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post , id = self.kwargs['post_id'])
        return context
    
    # def create_comment(request , pk):
#     post = get_object_or_404(Post , pk = pk)
#     if request.method == 'POST':
#         comment = CommentForm(request.POST)
#         if comment.is_valid():
#             #we should make (commit = False) to let django set the user and post ids before saving the comment form  
#             comment = comment.save(commit = False)
#             comment.author = request.user
#             comment.post = post
#             comment.save()
#             return redirect('post_detail' , pk = post.pk)
            
#     else:
#         comment = CommentForm()
#     return render(request , 'blog/comment_form.html' , {'comment':comment , 'post':post})
class CommentUpdateView(UpdateView , LoginRequiredMixin , UserPassesTestMixin):
    model = Comment
    fields = ['content']
    template_name = 'blog/comment_update.html'
    success_url = reverse_lazy('blog')
    
    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user
    
class CommentDeleteView(DeleteView , LoginRequiredMixin , UserPassesTestMixin):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'
    success_url = reverse_lazy('blog')
    
    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user