# Generated by Django 3.2 on 2021-04-23 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Librarian',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
