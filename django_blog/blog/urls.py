from django.urls import path
from . import views
from .views import DetailView , CreateView , ListView , UpdateView , DeleteView

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('post/new/', CreateView.as_view(), name='post_create'),
    path('blogs/', ListView.as_view(), name='blog'),
    path('post_list/<int:pk>/', DetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', UpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', DeleteView.as_view(), name='post_delete'),
    path('create_comment/<int:pk>/', views.create_comment , name='create_comment'),

]