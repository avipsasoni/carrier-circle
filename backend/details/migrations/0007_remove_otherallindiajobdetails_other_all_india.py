# Generated by Django 2.1.1 on 2018-10-07 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0006_auto_20181006_1337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otherallindiajobdetails',
            name='other_all_india',
        ),
    ]