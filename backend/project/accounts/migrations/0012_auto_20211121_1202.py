# Generated by Django 3.2.9 on 2021-11-21 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_rename_image_user_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_personal',
            new_name='business',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='location',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='birth_date',
            new_name='dateOfBirth',
        ),
    ]
