from django.db import models
from library_api import settings


class Book(models.Model):
    """
    Модель для представления книги в библиотеке.
    """

    title = models.TextField(
        verbose_name="Название книги", help_text="Введите название книги"
    )
    author = models.ForeignKey(
        "Author",
        on_delete=models.SET_NULL,
        verbose_name="Автор",
        help_text="Укажите автора книги",
        blank=True,
        null=True,
    )
    genre = models.TextField(
        verbose_name="Жанр",
        help_text="Укажите жанр книги",
        blank=True,
        null=True,
    )
    published_year = models.IntegerField(
        verbose_name="Год издания", help_text="Укажите год издания"
    )
    publisher = models.CharField(
        max_length=255,
        verbose_name="Издатель",
        help_text="Укажите издательство",
    )
    quantity = models.IntegerField(
        verbose_name="Количество экземпляров",
        help_text="Укажите количество экземпляров книги",
        default=1,
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления"
    )

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title


class Author(models.Model):
    """
    Модель для представления автора книги.
    """

    name = models.CharField(
        max_length=255,
        verbose_name="Имя автора",
        help_text="Введите имя автора",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления"
    )

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return self.name


class BookIssue(models.Model):
    """
    Модель для представления выдачи книги пользователю.
    """

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        verbose_name="Книга",
        help_text="Выберите книгу, которую выдают",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        help_text="Выберите пользователя, которому выдают книгу",
    )
    issue_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата выдачи",
        help_text="Дата, когда книга была выдана",
    )
    return_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Дата возврата",
        help_text="Дата, когда книга была возвращена",
    )
    is_returned = models.BooleanField(
        default=False,
        verbose_name="Возвращена",
        help_text="Статус возврата книги",
    )

    class Meta:
        verbose_name = "Выдача книги"
        verbose_name_plural = "Выдачи книг"

    def __str__(self):
        return f"{self.book.title} выдана {self.user.username}"
