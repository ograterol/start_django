# -*- coding: utf-8 -*-

# future
from __future__ import unicode_literals

# Django
from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext_lazy as _


class UserLoginForm(forms.Form):
    """
    Display the login form.
    """

    _user = None

    username = forms.CharField(label=('Username'))
    password = forms.CharField(widget=forms.PasswordInput, label=('Password'))

    def authenticate_user(self):
        username = self.cleaned_data.get('username', False)
        password = self.cleaned_data.get('password', False)

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")

            if user is not None:
                self._user = user
                return True

        return False

    def clean(self):
        found = self.authenticate_user()

        if not found:
            raise Exception()

    def get_user(self):
        return self._user


class RegisterUserForm(forms.ModelForm):
    """
    Display the register form.
    """

    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
                                widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email']

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if password and password2 and password != password2:
            raise forms.ValidationError(u"Passwords do not match.")

        return password2


class UserUpdateForm(forms.ModelForm):
    """
    Display the user update form.
    """

    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name']

    def clean(self, *args, **kwargs):
        cleaned_data = super(UserUpdateForm, self).clean(*args, **kwargs)
        return cleaned_data


class AddUserForm(forms.ModelForm):
    """
    Display the user add form.
    """
    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'username']

    def clean(self, *args, **kwargs):
        cleaned_data = super(AddUserForm, self).clean(*args, **kwargs)
        return cleaned_data
