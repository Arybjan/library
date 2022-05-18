# Generated by Django 4.0.4 on 2022-05-18 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_alter_user_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('release_date', models.DateField(verbose_name='Дата выпуска')),
                ('words_num', models.IntegerField(verbose_name='Количество слов')),
                ('pages_num', models.IntegerField(verbose_name='Количество страниц')),
                ('is_premium', models.BooleanField(verbose_name='Премиум')),
                ('created_at', models.DateTimeField(verbose_name='Время создания')),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Difficulty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Сложность')),
            ],
        ),
        migrations.CreateModel(
            name='Formats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Формат')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130, verbose_name='Жанр')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Язык')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=190, verbose_name='Теги')),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.IntegerField(verbose_name='Страница')),
                ('word_from', models.IntegerField(verbose_name='Слово от')),
                ('word_to', models.IntegerField(verbose_name='Слово для')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(verbose_name='Время создания')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name='Время создания')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='CountryLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.country')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.language')),
            ],
        ),
        migrations.CreateModel(
            name='BookTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name='Время создания')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.tags')),
            ],
        ),
        migrations.CreateModel(
            name='BookGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name='Время создания')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.genre')),
            ],
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name='Время создания')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.categories')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='difficulty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.difficulty'),
        ),
        migrations.AddField(
            model_name='book',
            name='format',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.formats'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.language'),
        ),
    ]
