from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views
from .views import CustomLoginView, RegisterView, ChangePasswordView
from .forms import LoginForm

urlpatterns = [
    path('home/', views.home_page, name='home_page'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='accounts/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('registration/', RegisterView.as_view(), name='users-registration'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]