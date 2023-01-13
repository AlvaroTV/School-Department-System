# Generated by Django 4.1.1 on 2023-01-04 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0010_actualizacion_anteproyecto_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='actualizacion_anteproyecto',
            name='tipo',
            field=models.CharField(choices=[('ACTUALIZADO', 'ACTUALIZADO'), ('REMOVIDO', 'REMOVIDO')], default='ACTUALIZADO', max_length=15),
        ),
    ]