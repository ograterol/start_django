# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# admin.site.register(User)

@admin.register(User)
class UserAdmin(UserAdmin):
	list_display = ('username', 'is_staff', 'id')