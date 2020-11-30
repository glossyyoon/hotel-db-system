# Generated by Django 3.1.3 on 2020-11-30 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
        ('RoomApp', '0004_auto_20201130_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_roomid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='RoomApp.room'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_userid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='UserApp.guest'),
        ),
    ]
