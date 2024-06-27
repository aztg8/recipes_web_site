# Generated by Django 4.1.6 on 2024-03-28 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0003_recipe_description_alter_instruction_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='profiles/', verbose_name='Фото')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('address', models.CharField(max_length=150, verbose_name='Адрес')),
                ('job', models.CharField(max_length=30, verbose_name='Профессия')),
                ('telegram', models.CharField(max_length=30, verbose_name='Ник в телеграме')),
                ('instagram', models.CharField(max_length=30, verbose_name='Ник в инстаграме')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]
