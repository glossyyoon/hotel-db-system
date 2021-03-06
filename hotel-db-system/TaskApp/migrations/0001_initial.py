# Generated by Django 3.1.3 on 2020-11-28 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserApp', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_item', models.CharField(max_length=100)),
                ('product_count', models.IntegerField(default=1)),
                ('product_from', models.DateTimeField(auto_now=True)),
                ('product_to', models.DateTimeField()),
                ('staff_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='UserApp.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Room_Cleaning', 'Room_Cleaning'), ('Room_Service', 'Room_Service'), ('Room_Error', 'Room_Error'), ('Room_ETC', 'Room_ETC'), ('Carry_In', 'Carry_In'), ('Carry_Out', 'Carry_Out'), ('Valet_Parking', 'Valet_Parking'), ('Product_Purchasing', 'Product_Purchasing'), ('Carry_Room_Service', 'Carry_Room_Service'), ('ETC', 'ETC')], max_length=50)),
                ('date_time', models.DateTimeField()),
                ('completed_date_time', models.DateTimeField(blank=True, null=True)),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(choices=[('Not_Assigned', 'Not_Assigned'), ('Wait_For_Accept', 'Wait_For_Accept'), ('Proceeding', 'Proceeding'), ('Completed', 'Completed')], max_length=50)),
                ('roomservice_num', models.IntegerField(blank=True, null=True)),
                ('charged_robot_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='charged_robot_id', to='UserApp.robot')),
                ('charged_staff_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='charged_staff_id', to='UserApp.staff')),
                ('product_request_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TaskApp.productrequest')),
                ('send_guest_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='send_guest_id', to='UserApp.guest')),
                ('send_staff_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='send_staff_id', to='UserApp.staff')),
            ],
        ),
    ]
