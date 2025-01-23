# Generated by Django 4.2.16 on 2025-01-22 17:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("library", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookissue",
            name="user",
            field=models.ForeignKey(
                help_text="Выберите пользователя, которому выдают книгу",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
        migrations.AddField(
            model_name="book",
            name="author",
            field=models.ForeignKey(
                blank=True,
                help_text="Укажите автора книги",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="library.author",
                verbose_name="Автор",
            ),
        ),
    ]
