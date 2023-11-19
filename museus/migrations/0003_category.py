# Generated by Django 4.2.7 on 2023-11-19 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museus', '0002_comment_delete_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('movies', models.ManyToManyField(to='museus.post')),
            ],
        ),
    ]