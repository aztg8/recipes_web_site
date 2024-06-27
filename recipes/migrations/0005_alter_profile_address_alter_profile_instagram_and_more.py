# Generated by Django 4.1.6 on 2024-03-28 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(default='**********', max_length=150, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='instagram',
            field=models.CharField(default='**********', max_length=30, verbose_name='Ник в инстаграме'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='job',
            field=models.CharField(default='**********', max_length=30, verbose_name='Профессия'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(default='**********', max_length=20, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='telegram',
            field=models.CharField(default='**********', max_length=30, verbose_name='Ник в телеграме'),
        ),
    ]