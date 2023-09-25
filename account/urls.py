
from django.urls import path
from . import views
urlpatterns = [
    path("register/", views.UserRegistrationView.as_view(), name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("profile/", views.UserProfileView.as_view(), name="profile"),
    path("change-password/", views.UserChangePassword.as_view(),
         name="changePassword"),
    path("send-rest-password-email/",
         views.SendPasswordResetEmailView.as_view(), name="passwordReset"),
    path("reset-password/<uid>/<token>/",
         views.UserPasswordResetView.as_view(), name="reset-password"),
]
