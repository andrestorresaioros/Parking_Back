# Generated by Django 4.2.3 on 2023-07-11 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0003_remove_client_id_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='cost',
        ),
        migrations.AddField(
            model_name='client',
            name='identification',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='receipt',
            name='cost',
            field=models.CharField(default='', max_length=200),
        ),
    ]