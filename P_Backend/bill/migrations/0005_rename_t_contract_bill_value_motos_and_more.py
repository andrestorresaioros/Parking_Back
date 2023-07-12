# Generated by Django 4.2.3 on 2023-07-11 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Parking', '0003_remove_type_parking_id_parking_delete_space_and_more'),
        ('bill', '0004_delete_admin_bill_id_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill',
            old_name='t_contract',
            new_name='value_Motos',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='date_entry',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='date_exit',
        ),
        migrations.AddField(
            model_name='bill',
            name='id_Parking',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Parking.parking'),
        ),
        migrations.AddField(
            model_name='bill',
            name='values_Autos',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='bill',
            name='values_Day',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='bill',
            name='values_Heavys',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='bill',
            name='values_Month',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='bill',
            name='values_Week',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='bill',
            name='values_Year',
            field=models.CharField(default='', max_length=200),
        ),
    ]
