# Generated by Django 3.2.9 on 2021-11-16 13:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Save',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('pin_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pins.pin', verbose_name='Pin saved')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]