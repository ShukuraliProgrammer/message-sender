from django.contrib import admin
from .models import UserModel, Message
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.admin import UserAdmin

admin.site.unregister(Group)


class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("telegram_id", "birth_day", "username")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = ("telegram_id", "birth_day", "username")


@admin.register(UserModel)
class UserModelAdmin(UserAdmin):
    list_display = ("id", "telegram_id", "birth_day", "username", "password")
    add_form = CustomUserCreateForm
    form = CustomUserChangeForm
    fieldsets = (
        (None, {"fields": ("username", "password", "birth_day", "telegram_id")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("telegram_id", "birth_day", "username", "password1", "password2"),
            },
        ),
    )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "text")
