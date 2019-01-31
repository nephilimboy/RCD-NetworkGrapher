# Generated by Django 2.1.5 on 2019-01-31 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grapherEntities', '0001_initial'),
        ('grapher', '0009_remove_logparser_grapherentity'),
    ]

    operations = [
        migrations.AddField(
            model_name='logparser',
            name='grapherEntity',
            field=models.ManyToManyField(blank=True, related_name='logParsers_list', to='grapherEntities.GrapherEntity'),
        ),
    ]
