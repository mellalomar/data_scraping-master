# Generated by Django 2.1.7 on 2021-04-07 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['created_date']},
        ),
        migrations.RemoveField(
            model_name='job',
            name='location',
        ),
        migrations.RemoveField(
            model_name='job',
            name='title',
        ),
        migrations.RemoveField(
            model_name='job',
            name='url',
        ),
        migrations.AddField(
            model_name='job',
            name='encours',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='taux',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='volume',
            field=models.IntegerField(default=0),
        ),
    ]
