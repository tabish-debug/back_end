# Generated by Django 4.0.1 on 2022-02-27 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='redditpost',
            name='job_id',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='twitterpost',
            name='job_id',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
