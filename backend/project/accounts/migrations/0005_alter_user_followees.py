# Generated by Django 3.2.9 on 2021-11-16 15:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_followees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='followees',
            field=models.ManyToManyField(through='accounts.Following', to=settings.AUTH_USER_MODEL, verbose_name='following'),
        ),
    ]