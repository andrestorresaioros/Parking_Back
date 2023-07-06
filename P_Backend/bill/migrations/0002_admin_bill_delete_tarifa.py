# Generated by Django 4.2.3 on 2023-07-06 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(default='', max_length=200)),
                ('contraseña', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zona', models.CharField(default='', max_length=200)),
                ('t_Contrato', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Tarifa',
        ),
    ]
