# Generated by Django 4.1.5 on 2023-02-24 11:20

from django.db import migrations

goals = [
    ("minigame", "minigame_catching", "Catch the rubbish, recycling or glass based on your bin! The higher the score, the more points you get.",
     0, 0, 'sustainable_app/img/catching_game.jpg', '/minigame_catching/'),
    ("minigame", "sorting", "Sort the rubbish, recycling and glass into their respective bins! The higher the score, the more points you get.",
     0, 0, 'sustainable_app/img/sorting_game.png', '/sorting/'),
    ("quiz", "Sustainable Quiz", "Answer these sustainable questions and get rewards.",
     100, 100, 'sustainable_app/img/quiz_game.png', '/quiz/'),
]


def make_goals(apps, schema_editor):
    Goal = apps.get_model('sustainable_app', 'Goal')

    # Add all items to database
    for [type, name, desc, xp, points, image, url] in goals:
        goal = Goal(type=type, name=name, description=desc, point_reward=points,
                    xp_reward=xp, image=image, url=url, active=False)
        goal.save()


def undo_make_goals(apps, schema_editor):
    Goal = apps.get_model('sustainable_app', 'Goal')
    for [type, name, desc, xp, points, image, url] in goals:
        try:
            goal = Goal.objects.get(type=type, name=name, description=desc,
                                    point_reward=points, xp_reward=xp, image=image, url=url, active=False)
            goal.delete()
        except Goal.DoesNotExist:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('sustainable_app', '0010_remove_dailydata_personal_goals_goal_active_and_more'),
    ]

    operations = [
        migrations.RunPython(make_goals, undo_make_goals)
    ]
