# Generated by Django 4.2 on 2024-07-24 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_proxymanager'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProxyEmployee2',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('testapp.employee',),
        ),
    ]
