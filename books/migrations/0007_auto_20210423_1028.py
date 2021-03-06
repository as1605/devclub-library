# Generated by Django 3.2 on 2021-04-23 10:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_issue_returned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='approvetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='request',
            name='requesttime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='return',
            name='returntime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
