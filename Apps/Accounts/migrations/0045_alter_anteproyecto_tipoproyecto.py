# Generated by Django 4.1.1 on 2022-10-13 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0044_alter_estudiante_numcelular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anteproyecto',
            name='tipoProyecto',
            field=models.CharField(choices=[('PROPUESTA PROPIA', 'PROPUESTA PROPIA'), ('BANCO DE PROYECTOS', 'BANCO DE PROYECTOS'), ('TRABAJADOR', 'TRABAJADOR')], default='ACTIVO', max_length=25),
        ),
    ]