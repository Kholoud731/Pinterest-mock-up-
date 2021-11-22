# Generated by Django 3.2.9 on 2021-11-19 08:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pins', '0015_alter_pin_react'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='react',
            field=models.ManyToManyField(blank=True, related_name='_pins_pin_react_+', to=settings.AUTH_USER_MODEL),
        ),
    ]