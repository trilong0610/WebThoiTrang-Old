# Generated by Django 3.1.3 on 2020-12-13 15:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20201213_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseproduct',
            name='time_create',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 13, 22, 42, 23, 127128)),
        ),
    ]
