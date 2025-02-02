# Generated by Django 4.2 on 2024-07-12 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movies', models.CharField(max_length=300)),
                ('year', models.IntegerField()),
                ('genre', models.CharField(max_length=300)),
                ('rating', models.FloatField()),
                ('oneLine', models.TextField()),
                ('stars', models.CharField(max_length=250)),
                ('votes', models.CharField(max_length=250)),
                ('runTime', models.FloatField()),
                ('gross', models.CharField(max_length=250)),
            ],
        ),
    ]
