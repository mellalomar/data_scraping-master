# Generated by Django 2.1.7 on 2021-04-07 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0004_auto_20210407_2139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('was_executed_before', models.BooleanField(default=False)),
            ],
        ),
    ]
