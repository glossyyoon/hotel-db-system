# Generated by Django 3.1.3 on 2020-11-24 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PadApp', '0004_auto_20201118_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomservicetype',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
