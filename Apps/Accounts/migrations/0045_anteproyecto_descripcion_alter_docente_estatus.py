# Generated by Django 4.1.1 on 2023-02-26 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0044_alter_residencia_numintegrantes'),
    ]

    operations = [
        migrations.AddField(
            model_name='anteproyecto',
            name='descripcion',
            field=models.CharField(default='Hola c:', max_length=500),
        ),
        migrations.AlterField(
            model_name='docente',
            name='estatus',
            field=models.CharField(choices=[('ACTIVO', 'ACTIVO'), ('VACACIONES', 'VACACIONES'), ('INACTIVO', 'INACTIVO')], default='ACTIVO', max_length=15),
        ),
    ]
