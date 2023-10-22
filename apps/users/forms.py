from typing import Any
from django import forms
from captcha.fields import ReCaptchaField
from django.contrib.auth import get_user_model
from captcha.widgets import ReCaptchaV2Checkbox
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserSignup(UserCreationForm):
	class Meta:
		model = get_user_model()
		fields = ["username", "email", "password1", "password2" ]

	def save(self, commit = False):
		user = super(UserSignup, self).save(commit = False)
		user.email = self.cleaned_data["email"]
		if commit:
			user.save()
		return user


class UserSignin(AuthenticationForm):
	def __init__(self, *args, **kwargs) -> None:
		super(UserSignin, self).__init__(*args, **kwargs)
	
	username = forms.CharField(widget = forms.TextInput())
	password = forms.CharField(widget = forms.PasswordInput())
	captcha = ReCaptchaField(
		widget= ReCaptchaV2Checkbox(
			attrs={
				'data-theme': 'dark',
				'data-size': 'normal',
			}
		)
	)

class UserUpdate(forms.ModelForm):
	class Meta:
		model = get_user_model()
		fields = ["username", "first_name", "last_name", "image"]