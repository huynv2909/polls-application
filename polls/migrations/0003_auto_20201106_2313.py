# Generated by Django 3.1.3 on 2020-11-06 16:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20201106_0022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='vote',
            new_name='votes',
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 6, 16, 12, 33, 743607, tzinfo=utc)),
        ),
    ]
