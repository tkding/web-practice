# Generated by Django 4.2.3 on 2023-07-11 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_pasenger'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pasenger',
            new_name='Passenger',
        ),
    ]
