# Generated by Django 4.1.5 on 2023-02-19 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('salt', models.CharField(max_length=200)),
                ('xp', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('weekly_xp', models.IntegerField(default=0)),
            ],
        ),
    ]
