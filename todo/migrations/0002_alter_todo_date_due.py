# Generated by Django 3.2.12 on 2023-01-11 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_due',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
