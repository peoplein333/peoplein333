# Generated by Django 2.2.3 on 2019-09-29 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userExtends', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=30, verbose_name='name'),
        ),
    ]
