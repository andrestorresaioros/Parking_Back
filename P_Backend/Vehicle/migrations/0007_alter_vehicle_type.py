# Generated by Django 4.2.3 on 2023-07-14 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicle', '0006_alter_vehicle_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='type',
            field=models.CharField(choices=[('Automóvil', 'Automóvil'), ('Motocicleta', 'Motocicleta'), ('Vehículos Pesados', 'Vehículos Pesados')], default='', max_length=200),
        ),
    ]
