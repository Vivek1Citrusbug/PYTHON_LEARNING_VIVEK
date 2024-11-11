from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput

# - Create/Register a user (Model Form)
class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    class meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
    
# Authenticate a user (Model form)
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(),required=True)
    password = forms.CharField(widget=PasswordInput(), required=True)