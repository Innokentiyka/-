# Generated by Django 5.0.4 on 2024-04-23 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='habit',
            options={'ordering': ['name', 'place', 'action'], 'verbose_name': 'привычка', 'verbose_name_plural': 'привычки'},
        ),
    ]
