# -*- coding: utf-8 -*-

# future
from __future__ import unicode_literals

# Django
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (
    LoginRequiredMixin
)
from django.shortcuts import render, redirect
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView)
from django.utils.translation import gettext as _
from django.urls import reverse_lazy

# Rest_Framework
from rest_framework import parsers, status, renderers
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken

# Local Django
from base.mixin import StaffRequiredMixin, UserPerfilMixin

from .forms import (
    UserLoginForm,
    RegisterUserForm,
    UserUpdateForm,
    AddUserForm
)

from .models import User

from .serializers import (
    AuthCustomTokenSerializer,
    UsersSerializer
)


@login_required
def index(request):
    """
    Display the index page.
    """

    model = get_user_model()
    return render(request, 'users/index.html')


def login_view(request):
    """
    Display the login form and handle the login action.
    """
    form = UserLoginForm()

    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
        return redirect('user:index')
    else:
        form = UserLoginForm()

    return render(request, "users/form.html", {"form": form})


class RegisterUserView(CreateView):
    """
    Display the register form and handle the register action.
    """

    form_class = RegisterUserForm
    template_name = "users/register.html"

    def form_valid(self, form):

        user = form.save(commit=False)
        password = form.cleaned_data.get('password', False)
        if password:
            user.set_password(password)
            user.save()
            new_user = authenticate(username=user, password=password)
            login(self.request, new_user)
            return redirect('user:index')


def logout_view(request):
    """
    Handle the logout action.
    """

    logout(request)
    return redirect('user:login')


class AddUserView(StaffRequiredMixin, CreateView):
    """
    Display the add new user form by admin and handle the new register action.
    """

    form_class = AddUserForm
    template_name = 'users/add_user.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        if form.cleaned_data:
            user.save()
            return redirect('user:user-list')


class UserListView(StaffRequiredMixin, ListView):
    """
    Display user list.
    """

    model = get_user_model()
    template_name = 'users/user_list.html'


class UserDetailView(LoginRequiredMixin, DetailView):
    """
    Display user details.
    """

    model = get_user_model()
    template_name = 'users/profile.html'


class UserUpdateView(LoginRequiredMixin, UserPerfilMixin, UpdateView):
    """
    Handle user update action.
    """

    model = get_user_model()
    form_class = UserUpdateForm
    template_name = "users/user_update.html"
    success_url = 'user:profile'

    def get_success_url(self):
        return reverse_lazy(
            self.success_url, kwargs={'pk': self.object.id})


class UserDeleteView(StaffRequiredMixin, DeleteView):
    """
    Handle user delete action.
    """

    model = get_user_model()
    template_name = "users/user_delete.html"
    success_url = reverse_lazy('user:user-list')


class Login(ObtainAuthToken, APIView):
    """
    Display the login form and handle the register action with Angular v4.
    """

    serializer_class = AuthCustomTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.is_valid():
            user = serializer.data['user']
            password = serializer.data['password']
            new_user = authenticate(username=user, password=password)

            if new_user:
                token, created = Token.objects.get_or_create(
                    user=new_user)

                return Response(
                    {
                        'created': created,
                        'token': token.key,
                    }
                )
            else:
                content = {
                    'detail': _('Unable to login with provided credentials.')
                }
                return Response(content, status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class Register(ObtainAuthToken, APIView):
    """
    Display the register form and handle the register action with Angular v4.
    """

    serializer_class = UsersSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.is_valid():
            user = serializer.data['user']
            password = serializer.data['password']
            password2 = serializer.data['password2']

            if password and password2 and password != password2:
                content = {
                    'detail': _('Passwords do not match.')
                }
                return Response(content, status=status.HTTP_401_UNAUTHORIZED)
            else:
                new_user = User(username=user)
                new_user.set_password(password)
                new_user.save()
                new_auth = authenticate(username=user, password=password)

                if new_auth:
                    token, created = Token.objects.get_or_create(
                        user=new_auth)

                    return Response(
                        {
                            'created': created,
                            'token': token.key,
                        }
                    )
                else:
                    content = {
                        'detail': _('Unable to login with provided credentials.')
                    }
                    return Response(content,
                                    status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
