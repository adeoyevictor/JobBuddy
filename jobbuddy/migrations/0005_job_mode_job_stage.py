# Generated by Django 4.2.2 on 2023-07-24 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobbuddy', '0004_job_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='mode',
            field=models.CharField(choices=[('FULL_TIME', 'FULL_TIME'), ('PART_TIME', 'PART_TIME'), ('CONTRACT', 'CONTRACT')], default=('FULL_TIME', 'FULL_TIME'), max_length=64),
        ),
        migrations.AddField(
            model_name='job',
            name='stage',
            field=models.CharField(choices=[('NOT_APPLIED', 'NOT_APPLIED'), ('APPLIED', 'APPLIED'), ('FIRST_INTERVIEW', 'FIRST_INTERVIEW'), ('FOLLOW_UP_INTERVIEWS', 'FOLLOW_UP_INTERVIEWS'), ('OFFER', 'OFFER')], default=('NOT_APPLIED', 'NOT_APPLIED'), max_length=64),
        ),
    ]