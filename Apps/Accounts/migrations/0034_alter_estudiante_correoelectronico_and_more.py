# Generated by Django 4.1.1 on 2023-01-18 16:37

import Apps.Accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0033_alter_anteproyecto_estatus_alter_residencia_estatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='correoElectronico',
            field=models.EmailField(blank=True, error_messages={'unique': 'Existe otro estudiante con este correo electrónico.'}, max_length=70, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='numControl',
            field=models.CharField(blank=True, error_messages={'unique': 'Existe otro estudiante con este número de control. '}, max_length=10, unique=True, validators=[Apps.Accounts.models.validate_len_num_control]),
        ),
    ]
