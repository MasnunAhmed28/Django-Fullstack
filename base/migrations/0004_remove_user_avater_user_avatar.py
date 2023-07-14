# Generated by Django 4.1.5 on 2023-05-15 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_user_avater'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avater',
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.TextField(default='avatar.svg', null=True),
        ),
    ]
