from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
	email = forms.EmailField()
	firstname = forms.CharField(max_length=100)
	lastname = forms.CharField(max_length=100)


	class Meta:
		model = User
		fields = ['username', 'firstname', 'lastname', 'email',  'password1', 'password2']
