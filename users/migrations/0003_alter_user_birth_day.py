# Generated by Django 4.2.4 on 2023-09-03 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_email_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_day',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
    ]