# Generated by Django 4.2.3 on 2023-07-08 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0002_client_id_admin_contract_id_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='id_Admin',
        ),
    ]