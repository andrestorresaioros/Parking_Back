# Generated by Django 4.2.3 on 2023-07-11 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Parking', '0002_parking_id_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type_parking',
            name='id_Parking',
        ),
        migrations.DeleteModel(
            name='Space',
        ),
        migrations.DeleteModel(
            name='Type_Parking',
        ),
    ]
