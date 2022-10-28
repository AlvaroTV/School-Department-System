# Generated by Django 4.1.1 on 2022-10-28 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0079_alter_docente_fotousuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anteproyecto',
            name='estatus',
            field=models.CharField(blank=True, choices=[('ENVIADO', 'ENVIADO'), ('PENDIENTE', 'PENDIENTE'), ('EN REVISION', 'EN REVISION'), ('ACEPTADO', 'ACEPTADO'), ('RECHAZADO', 'RECHAZADO')], default='ENVIADO', max_length=15),
        ),
    ]
