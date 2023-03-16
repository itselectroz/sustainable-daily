# Generated by Django 4.1.5 on 2023-03-16 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sustainable_app', '0009_merge_migrations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='quizquestion',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
