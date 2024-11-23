from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from.views import ObtainAuthTokenView

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')


urlpatterns = [
   path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
   path('', include(router.urls)),  # This includes all routes registered with the router
   path('token/', ObtainAuthTokenView.as_view(), name='token'),
]
