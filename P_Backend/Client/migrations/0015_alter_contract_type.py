# Generated by Django 4.2.3 on 2023-07-14 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0014_alter_contract_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='type',
            field=models.CharField(choices=[('dia', 'Día'), ('semana', 'Semana'), ('mes', 'Mes'), ('año', 'Año')], default='', max_length=200),
        ),
    ]
