# Generated by Django 3.2.9 on 2021-11-21 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pins', '0018_rename_creator_id_pin_creator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pin',
            old_name='time_created',
            new_name='created_at',
        ),
    ]
