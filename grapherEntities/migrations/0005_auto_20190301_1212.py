# Generated by Django 2.1.5 on 2019-03-01 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grapherEntities', '0004_grapherentity_logparser_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grapherentityextradetails',
            name='grapherEntity',
        ),
        migrations.DeleteModel(
            name='GrapherEntityExtraDetails',
        ),
    ]
