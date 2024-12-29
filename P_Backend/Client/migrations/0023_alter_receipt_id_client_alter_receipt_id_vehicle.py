# Generated by Django 4.2.3 on 2023-07-18 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicle', '0007_alter_vehicle_type'),
        ('Client', '0022_alter_receipt_id_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='id_Client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.client'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='id_Vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Receipt_Vehicle', to='Vehicle.vehicle'),
        ),
    ]