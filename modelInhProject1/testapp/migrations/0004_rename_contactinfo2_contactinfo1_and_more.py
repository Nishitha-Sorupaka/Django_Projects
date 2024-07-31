# Generated by Django 4.2 on 2024-07-23 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_contactinfo2_delete_contactinfo1_delete_student1_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactInfo2',
            new_name='ContactInfo1',
        ),
        migrations.RenameModel(
            old_name='Student2',
            new_name='Student1',
        ),
        migrations.RenameModel(
            old_name='Teacher2',
            new_name='Teacher1',
        ),
        migrations.RenameField(
            model_name='student1',
            old_name='contactinfo2_ptr',
            new_name='contactinfo1_ptr',
        ),
        migrations.RenameField(
            model_name='teacher1',
            old_name='contactinfo2_ptr',
            new_name='contactinfo1_ptr',
        ),
    ]
