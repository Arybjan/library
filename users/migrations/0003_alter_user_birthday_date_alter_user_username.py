# Generated by Django 4.0.4 on 2022-05-17 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_country_id_cities_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday_date',
            field=models.DateField(verbose_name='День рождения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, verbose_name='Имя пользователя'),
        ),
    ]
