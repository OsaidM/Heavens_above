# Generated by Django 2.2.4 on 2020-12-23 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heaven_app', '0002_auto_20201223_1055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='description',
            new_name='content',
        ),
    ]
