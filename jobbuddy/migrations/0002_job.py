# Generated by Django 4.2.3 on 2023-07-24 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobbuddy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('company', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=64)),
                ('url', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('color', models.CharField(choices=[('#5350E3', '#5350E3'), ('#25ADE7', '#25ADE7'), ('#2AD587', '#2AD587'), ('#FFF500', '#FFF500'), ('#FF7C00', '#FF7C00'), ('#E350D8', '#E350D8'), ('#9012FE', '#9012FE')], default=('#5350E3', '#5350E3'), max_length=7)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
