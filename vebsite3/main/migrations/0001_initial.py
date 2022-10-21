# Generated by Django 4.1.2 on 2022-10-19 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('task', models.TextField(verbose_name='Описание')),
                ('text', models.TextField(verbose_name='Текст')),
                ('image', models.FileField(upload_to='', verbose_name='Изображение')),
            ],
        ),
    ]
