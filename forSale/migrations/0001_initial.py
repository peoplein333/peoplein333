# Generated by Django 2.2.3 on 2019-09-28 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('desc', models.TextField(blank=True)),
                ('price', models.PositiveIntegerField(default=0)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]