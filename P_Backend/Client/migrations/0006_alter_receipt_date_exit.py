# Generated by Django 4.2.3 on 2023-07-11 17:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0005_receipt_id_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='date_exit',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
