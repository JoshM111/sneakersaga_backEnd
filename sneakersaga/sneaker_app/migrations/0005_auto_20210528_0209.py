# Generated by Django 2.2 on 2021-05-28 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sneaker_app', '0004_auto_20210525_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sneaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('release_year', models.DateTimeField()),
                ('release_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('liked_by', models.ManyToManyField(blank=True, related_name='favorite_shoe', to='sneaker_app.User')),
            ],
        ),
        migrations.DeleteModel(
            name='Api',
        ),
    ]
