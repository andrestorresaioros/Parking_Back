# Generated by Django 4.2.3 on 2023-07-17 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0016_alter_contract_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='type',
            field=models.CharField(choices=[('Minuto', 'Minuto'), ('Día', 'Día'), ('Semana', 'Semana'), ('Mes', 'Mes'), ('Año', 'Año')], default='', max_length=200),
        ),
    ]
