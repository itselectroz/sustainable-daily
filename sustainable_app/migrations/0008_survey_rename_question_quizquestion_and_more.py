# Generated by Django 4.1.5 on 2023-03-14 18:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sustainable_app', '0008_create_personal_goals'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('currentlyActive', models.BooleanField(default=False)),
                ('survey_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='Question',
            new_name='QuizQuestion',
        ),
        migrations.AlterField(
            model_name='dailydata',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.CreateModel(
            name='SurveyQuestion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('Survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sustainable_app.survey')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyChoice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sustainable_app.surveyquestion')),
            ],
        ),
        migrations.AddField(
            model_name='survey',
            name='goal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sustainable_app.goal'),
        ),
    ]
