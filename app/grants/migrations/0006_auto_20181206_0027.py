# Generated by Django 2.1.2 on 2018-12-06 00:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0005_merge_20181204_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='next_contribution_date',
            field=models.DateField(default=datetime.datetime(1990, 1, 1, 0, 0), help_text='The next contribution date'),
        ),
    ]