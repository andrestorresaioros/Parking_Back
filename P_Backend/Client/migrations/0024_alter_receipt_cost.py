# Generated by Django 4.2.3 on 2023-07-19 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0023_alter_receipt_id_client_alter_receipt_id_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]
