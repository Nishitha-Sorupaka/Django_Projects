# Generated by Django 4.2 on 2024-07-11 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MOVIES', models.CharField(max_length=300)),
                ('YEAR', models.IntegerField()),
                ('GENRE', models.CharField(max_length=300)),
                ('RATING', models.FloatField()),
                ('ONELINE', models.TextField()),
                ('STARS', models.CharField(max_length=250)),
                ('VOTES', models.CharField(max_length=250)),
                ('RunTime', models.FloatField()),
                ('Gross', models.CharField(max_length=250)),
            ],
        ),
    ]
