# Generated by Django 4.2 on 2024-07-06 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_rename_student1_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
