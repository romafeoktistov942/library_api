from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Кастомная модель пользователя, использующая email вместо username.
    """

    username = None
    email = models.CharField(
        max_length=150,
        verbose_name="Почта",
        help_text="Введите почту",
        unique=True,
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        help_text="Введите номер телефона",
        blank=True,
        null=True,
    )

    def __str__(self):
        """
        Возвращает строковое представление пользователя.
        """
        return f"{self.first_name} {self.last_name}: {self.email}"

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        """
        Метаданные для модели User.
        """

        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
