# Generated by Django 4.0.1 on 2022-02-25 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messagesender',
            old_name='sender_id',
            new_name='sender',
        ),
    ]