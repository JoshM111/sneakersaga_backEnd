# Generated by Django 2.2 on 2021-05-25 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sneaker_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='liked_by',
            field=models.ManyToManyField(related_name='favorite_shoe', to='sneaker_app.User'),
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
    ]
