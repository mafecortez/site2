# Generated by Django 4.2.7 on 2023-11-19 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museus', '0003_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='movies',
            new_name='posts',
        ),
    ]
