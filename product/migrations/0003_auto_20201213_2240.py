# Generated by Django 3.1.3 on 2020-12-13 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20201213_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
