from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Админ-класс для модели User.
    """

    list_filter = ["id", "email"]
