# Generated by Django 3.1.3 on 2020-11-17 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='birthday',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='staff',
            name='hire_date',
            field=models.DateField(),
        ),
    ]
