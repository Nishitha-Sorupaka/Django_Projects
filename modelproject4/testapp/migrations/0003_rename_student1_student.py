# Generated by Django 4.2 on 2024-07-06 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_rename_student_student1'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student1',
            new_name='Student',
        ),
    ]
