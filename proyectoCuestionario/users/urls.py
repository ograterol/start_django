from django.conf.urls import url
from . import views
from views import (
    RegisterUserView,
    UserListView,
    UserDetailView,
    UserUpdateView,
    UserDeleteView,
    AddUserView
)

urlpatterns = [
    url(
        r'^$',
        views.index,
        name='index'
    ),
    url(
        r'^login/$',
        views.login_view,
        name='login'
    ),
    url(
        r'^register/$',
        view=RegisterUserView.as_view(),
        name='register'
    ),
    url(
        r'^logout/$',
        view=views.logout_view,
        name='logout'
    ),
    url(
        r'^user_list/$',
        view=UserListView.as_view(),
        name='user-list'
    ),
    url(
        r'^profile/(?P<pk>[^\/]+)/$',
        view=UserDetailView.as_view(),
        name='profile'
    ),
    url(
        r'^profile/edit/(?P<pk>[^\/]+)/$',
        view=UserUpdateView.as_view(),
        name='profile-update'
    ),
    url(
        r'^profile/delete/(?P<pk>[^\/]+)/$',
        view=UserDeleteView.as_view(),
        name='profile-delete'
    ),
    url(
        r'^add_User/$',
        view=AddUserView.as_view(),
        name='add-user'
    ),
]