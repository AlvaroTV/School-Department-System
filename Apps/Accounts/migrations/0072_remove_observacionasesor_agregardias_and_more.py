# Generated by Django 4.1.1 on 2022-10-27 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0071_remove_observacion_observacionasesor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='observacionasesor',
            name='agregarDias',
        ),
        migrations.AddField(
            model_name='observacion',
            name='agregarDias',
            field=models.PositiveIntegerField(default=0),
        ),
    ]