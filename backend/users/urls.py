from django.urls import path
from .views import RegisterView, UserDetailView

urlpatterns = [
    # Signup endpoint
    path("signup/", RegisterView.as_view(), name="signup"),

    # Optional: get user profile (requires auth)
    path("me/", UserDetailView.as_view(), name="user-detail"),
]
