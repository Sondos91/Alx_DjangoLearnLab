# accounts/urls.py
from django.urls import path
from .views import UserRegistrationView, CustomAuthToken

urlpatterns = [
    # URL for user registration
    path('register/', UserRegistrationView.as_view(), name='user-registration'),

    # URL for login (authentication via token)
    path('login/', CustomAuthToken.as_view(), name='token-login'),
]


#["unfollow/<int:user_id>/", "follow/<int:user_id>"]