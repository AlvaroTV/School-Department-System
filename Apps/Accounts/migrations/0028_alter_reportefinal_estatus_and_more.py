# Generated by Django 4.1.1 on 2022-10-06 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0027_alter_expediente_manualdoc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportefinal',
            name='estatus',
            field=models.CharField(choices=[('ENVIADO', 'ENVIADO'), ('PENDIENTE', 'PENDIENTE'), ('REVISADO', 'REVISADO'), ('ACEPTADO', 'ACEPTADO'), ('RECHAZADO', 'RECHAZADO')], default='ENVIADO', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='reporteparcial1',
            name='estatus',
            field=models.CharField(choices=[('ENVIADO', 'ENVIADO'), ('PENDIENTE', 'PENDIENTE'), ('REVISADO', 'REVISADO'), ('ACEPTADO', 'ACEPTADO'), ('RECHAZADO', 'RECHAZADO')], default='ENVIADO', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='reporteparcial2',
            name='estatus',
            field=models.CharField(choices=[('ENVIADO', 'ENVIADO'), ('PENDIENTE', 'PENDIENTE'), ('REVISADO', 'REVISADO'), ('ACEPTADO', 'ACEPTADO'), ('RECHAZADO', 'RECHAZADO')], default='ENVIADO', max_length=15, null=True),
        ),
    ]
