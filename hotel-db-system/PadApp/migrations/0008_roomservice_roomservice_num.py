# Generated by Django 3.1.3 on 2020-11-25 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PadApp', '0007_roomservicetype_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomservice',
            name='roomservice_num',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]