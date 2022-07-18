from django.contrib import admin

from apps.user.models import CustomUser,Jwt


admin.site.register((CustomUser, Jwt))