# Generated by Django 2.1.5 on 2019-01-24 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GrapherEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GrapherEntityExtraDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=200)),
                ('grapherEntity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grapher_entity_extra_details', to='grapherEntities.GrapherEntity')),
            ],
        ),
    ]
