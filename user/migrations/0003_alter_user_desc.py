# Generated by Django 5.0.7 on 2024-07-11 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='desc',
            field=models.TextField(blank=True),
        ),
    ]
