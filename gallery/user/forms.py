from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
class LoginForm(AuthenticationForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for myField in self.fields:
        self.fields[myField].widget.attrs['class'] = 'form-control'
  


class SignupForm(UserCreationForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for myField in self.fields:
        self.fields[myField].widget.attrs['class'] = 'form-control'
  class Meta:
    model = User
    fields = ("username","email", "password1","password2")

  def save(self, commit=True):
    user = super(SignupForm, self).save(commit=False)
    user.email = self.cleaned_data['email']
    if commit:
      user.save()
    return user
