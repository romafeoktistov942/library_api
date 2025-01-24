# Generated by Django 4.2.16 on 2025-01-24 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="published_year",
        ),
        migrations.RemoveField(
            model_name="book",
            name="publisher",
        ),
        migrations.RemoveField(
            model_name="book",
            name="quantity",
        ),
        migrations.AddField(
            model_name="book",
            name="copies_count",
            field=models.PositiveIntegerField(
                default=1,
                help_text="Введите количество экземпляров книги",
                verbose_name="Количество экземпляров",
            ),
        ),
        migrations.AddField(
            model_name="book",
            name="publication_year",
            field=models.PositiveIntegerField(
                default=2025,
                help_text="Введите год издания книги",
                verbose_name="Год издания",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="author",
            name="name",
            field=models.CharField(
                default="",
                help_text="Введите имя автора",
                max_length=255,
                verbose_name="Имя автора",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.ForeignKey(
                default=1,
                help_text="Выберите автора книги",
                on_delete=django.db.models.deletion.CASCADE,
                to="library.author",
                verbose_name="Автор",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="book",
            name="genre",
            field=models.CharField(
                default="",
                help_text="Введите жанр книги",
                max_length=100,
                verbose_name="Жанр книги",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="book",
            name="title",
            field=models.CharField(
                help_text="Введите название книги",
                max_length=255,
                verbose_name="Название книги",
            ),
        ),
    ]
