from django.contrib.auth import login
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy, reverse

from .forms import CustomUserCreationForm, LoginForm


def home_page(request):
    return render(request, 'home_page.html')


class CustomLoginView(LoginView):
    form_class = LoginForm

    def get_success_url(self):
        return reverse('home_page')


class RegisterView(View):
    form_class = CustomUserCreationForm
    template_name = 'accounts/registration.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            return redirect(to='home_page')

        return render(request, self.template_name, {'form': form})


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_message = "Hasło zostało zmienione"
    success_url = reverse_lazy('home_page')



'''
def register(request):
    if request.method == "GET":
        return render(
            request, 'users/register.html',
            {'form': CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('home_page'))
'''