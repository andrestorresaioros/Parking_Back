# Generated by Django 4.2.3 on 2023-07-14 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0011_receipt_id_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='identification',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
