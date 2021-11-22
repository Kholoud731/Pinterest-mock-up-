# Generated by Django 3.2.9 on 2021-11-16 19:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pins', '0011_alter_pin_react'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='react',
            field=models.ManyToManyField(related_name='reacts', to=settings.AUTH_USER_MODEL),
        ),
    ]