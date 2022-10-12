# Generated by Django 4.1.1 on 2022-10-06 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0028_alter_reportefinal_estatus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportefinal',
            name='estatus',
            field=models.CharField(blank=True, choices=[('ENVIADO', 'ENVIADO'), ('PENDIENTE', 'PENDIENTE'), ('REVISADO', 'REVISADO'), ('ACEPTADO', 'ACEPTADO'), ('RECHAZADO', 'RECHAZADO')], default='ENVIADO', max_length=15),
        ),
        migrations.AlterField(
            model_name='reporteparcial1',
            name='estatus',
            field=models.CharField(blank=True, choices=[('ENVIADO', 'ENVIADO'), ('PENDIENTE', 'PENDIENTE'), ('REVISADO', 'REVISADO'), ('ACEPTADO', 'ACEPTADO'), ('RECHAZADO', 'RECHAZADO')], default='ENVIADO', max_length=15),
        ),
        migrations.AlterField(
            model_name='reporteparcial2',
            name='estatus',
            field=models.CharField(blank=True, choices=[('ENVIADO', 'ENVIADO'), ('PENDIENTE', 'PENDIENTE'), ('REVISADO', 'REVISADO'), ('ACEPTADO', 'ACEPTADO'), ('RECHAZADO', 'RECHAZADO')], default='ENVIADO', max_length=15),
        ),
    ]