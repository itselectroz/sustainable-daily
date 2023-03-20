# Generated by Django 4.1.5 on 2023-02-24 11:20

from django.db import migrations

items = [
    (
        "character",
        [
            ("cat", 0, True, 3),
            ("fish", 200, True, 5),
            ("frog", 400, True, 7),
            ("bird", 600, True, 9),
            ("badger", 800, True, 0),
            ("fox", 1000, True, 11),
        ],
    ),
    (
        "accessory",
        [
            ("none", 0, False, 0),
            ("viking", 100, True, 0),
            ("party", 400, True, 0),
            ("crown", 600, True, 0),
        ],
    ),
    (
        "username_color",
        [
            ("u_black", 200, True, 0),
            ("u_green", 200, True, 0),
            ("u_purple", 200, True, 0),
            ("u_orange", 200, True, 0),
            ("u_blue", 200, True, 0),
        ],
    ),
    (
        "background_color",
        [
            ("b_white", 200, True, 0),
            ("b_blue", 200, True, 0),
            ("b_pink", 200, True, 0),
            ("b_grey", 200, True, 0),
            ("b_green", 200, True, 0),
        ],
    ),
]


def make_items(apps, schema_editor):
    Item = apps.get_model('sustainable_app', 'Item')

    # Add all items to database
    for (type, values) in items:
        for [name, cost, on_sale, unlock_level] in values:
            item = Item(type=type, name=name, cost=cost, on_sale=on_sale, unlock_level=unlock_level)
            item.save()


def undo_make_items(apps, schema_editor):
    Item = apps.get_model('sustainable_app', 'Item')
    for (type, values) in items:
        for [name, cost, on_sale, unlock_level] in values:
            try:
                item = Item.objects.get(
                    type=type, name=name, cost=cost, on_sale=on_sale, unlock_level=unlock_level)
                item.delete()
            except Item.DoesNotExist:
                pass


class Migration(migrations.Migration):

    dependencies = [
        ('sustainable_app', '0002_goal_item_user_equipped_items_user_owned_items'),
    ]

    operations = [
        migrations.RunPython(make_items, undo_make_items)
    ]
