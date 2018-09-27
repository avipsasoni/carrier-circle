# Generated by Django 2.1.1 on 2018-09-27 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0006_delete_policedefencejobs'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoliceDefenceJobs',
            fields=[
                ('police_defence_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.CharField(max_length=60)),
                ('last_date', models.CharField(max_length=60)),
                ('post_name', models.CharField(max_length=255)),
                ('education', models.CharField(max_length=255)),
                ('more_info', models.TextField()),
                ('requirement_board', models.CharField(max_length=255)),
                ('type', models.IntegerField()),
                ('job_id', models.IntegerField(blank=True, default=None, null=True)),
                ('join_id', models.IntegerField(blank=True, default=None, null=True)),
            ],
        ),
    ]
