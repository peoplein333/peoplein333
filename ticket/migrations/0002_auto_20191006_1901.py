# Generated by Django 2.1.5 on 2019-10-06 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Item',
            new_name='Ticket',
        ),
    ]
