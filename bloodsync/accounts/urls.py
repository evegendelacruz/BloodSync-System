from django.urls import path
from .views import (
    CustomLoginView, 
    RegistrationView, 
    dashboard, 
    registration_pending_view,
    password_reset1, 
    password_reset, 
    password_reset_confirm,
    approve_user_view
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('registration-pending/', registration_pending_view, name='registration_pending'),
    path('approve-user/<int:user_id>/', approve_user_view, name='approve_user'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('reset-password/', password_reset1, name='password_reset1'),
    path('reset-password/code/', password_reset, name='password_reset'),
    path('reset-password/confirm/', password_reset_confirm, name='password_reset_confirm'),
]