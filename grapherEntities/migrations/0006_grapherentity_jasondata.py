# Generated by Django 2.1.5 on 2019-03-01 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grapherEntities', '0005_auto_20190301_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='grapherentity',
            name='jasonData',
            field=models.TextField(null=True),
        ),
    ]
