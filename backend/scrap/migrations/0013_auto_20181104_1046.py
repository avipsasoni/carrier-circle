# Generated by Django 2.1.1 on 2018-11-04 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0012_auto_20181026_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allbankjobs',
            name='bank_name',
        ),
        migrations.AddField(
            model_name='allbankjobs',
            name='requirement_board',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='otherfinancialjobs',
            name='requirement_board',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]