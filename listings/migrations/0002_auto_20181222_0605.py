# Generated by Django 2.1.3 on 2018-12-21 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='is_publised',
            new_name='is_published',
        ),
    ]
