# Generated by Django 2.1.4 on 2019-02-14 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_number_votes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='number',
            old_name='votes',
            new_name='count',
        ),
    ]
