# Generated by Django 4.1.5 on 2023-03-11 17:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import sustainable_app.models.location


class Migration(migrations.Migration):

    dependencies = [
        ('sustainable_app', '0005_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyData',
            fields=[
                ('date', models.DateField(default=datetime.date.today, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='goal',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='location',
            name='image',
            field=models.ImageField(upload_to=sustainable_app.models.location.Location.path_and_rename),
        ),
        migrations.CreateModel(
            name='PersonalGoalStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sustainable_app.goal')),
                ('user_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sustainable_app.dailydata')),
            ],
        ),
        migrations.CreateModel(
            name='DailyGoalStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('score', models.IntegerField(default=0)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sustainable_app.goal')),
                ('user_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sustainable_app.dailydata')),
            ],
        ),
        migrations.AddField(
            model_name='dailydata',
            name='daily_goals',
            field=models.ManyToManyField(related_name='daily_goals', through='sustainable_app.DailyGoalStatus', to='sustainable_app.goal'),
        ),
        migrations.AddField(
            model_name='dailydata',
            name='personal_goals',
            field=models.ManyToManyField(related_name='personal_goals', through='sustainable_app.PersonalGoalStatus', to='sustainable_app.goal'),
        ),
        migrations.AddField(
            model_name='dailydata',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
