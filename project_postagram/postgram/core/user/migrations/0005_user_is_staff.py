# Generated by Django 5.0 on 2024-03-11 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_user', '0004_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]