# Generated by Django 3.1.3 on 2020-12-13 15:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20201213_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseproduct',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 13, 22, 40, 5, 236011)),
        ),
    ]
