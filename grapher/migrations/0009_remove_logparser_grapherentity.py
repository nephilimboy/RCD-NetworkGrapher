# Generated by Django 2.1.5 on 2019-01-31 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grapher', '0008_auto_20190128_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logparser',
            name='grapherEntity',
        ),
    ]
