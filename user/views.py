from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, UsernameField


# Create your views here.
class LoginView(LoginView):
    template_name = 'login.html'


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
        widgets = {
            # 'email': forms.EmailInput(attrs={'required': True})
        }


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        data = form.cleaned.data
        new_user = User.objects.create_user(
            username=data['username'],
            password=data['password'],
            email=data['email']
        )
        url = f"{'register_complete'}?username={new_user.username}"
        return redirect(url)

class RegisterComplete(TemplateView):
    template_name = 'register_complete.html'


class EditProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
