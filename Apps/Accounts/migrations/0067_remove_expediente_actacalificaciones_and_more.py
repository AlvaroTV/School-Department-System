# Generated by Django 4.1.1 on 2022-10-26 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0066_anteproyecto_anteproyectodoc_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expediente',
            name='actaCalificaciones',
        ),
        migrations.RemoveField(
            model_name='expediente',
            name='actaResidencia',
        ),
        migrations.RemoveField(
            model_name='expediente',
            name='cartaTerminacion',
        ),
        migrations.RemoveField(
            model_name='expediente',
            name='constanciaTerminacion',
        ),
        migrations.AddField(
            model_name='expediente',
            name='cartaLiberacion',
            field=models.FileField(blank=True, null=True, upload_to='records/cartaLiberacion/'),
        ),
        migrations.AddField(
            model_name='expediente',
            name='manualTecnico',
            field=models.FileField(blank=True, null=True, upload_to='records/manualTecnico/'),
        ),
        migrations.AddField(
            model_name='expediente',
            name='manualUsuario',
            field=models.FileField(blank=True, null=True, upload_to='records/manualUsuario/'),
        ),
        migrations.AddField(
            model_name='observacion',
            name='tiempoCorreccion',
            field=models.IntegerField(default=5),
        ),
    ]