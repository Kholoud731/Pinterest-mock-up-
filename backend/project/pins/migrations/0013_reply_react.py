# Generated by Django 3.2.9 on 2021-11-16 19:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pins', '0012_comment_react'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='react',
            field=models.ManyToManyField(related_name='_pins_reply_react_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
