# Generated by Django 2.1.5 on 2019-01-17 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grapher', '0002_jasonparser_jasonparseralias'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogParserCrudFormCustomPattern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(max_length=50)),
                ('parserType', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('patternType', models.CharField(max_length=50)),
                ('customPatternName', models.CharField(max_length=50)),
                ('logParser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logParser_crudForm_customPattern', to='grapher.LogParser')),
            ],
        ),
        migrations.CreateModel(
            name='LogParserCrudFormStaticPattern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(max_length=50)),
                ('parserType', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('logParser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logParser_crudForm_staticPattern', to='grapher.LogParser')),
            ],
        ),
        migrations.AlterField(
            model_name='jasonparseralias',
            name='jasonParser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jason_alias', to='grapher.JasonParser'),
        ),
    ]