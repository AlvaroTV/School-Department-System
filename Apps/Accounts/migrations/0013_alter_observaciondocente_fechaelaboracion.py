# Generated by Django 4.1.1 on 2023-01-04 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0012_alter_actualizacion_anteproyecto_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observaciondocente',
            name='fechaElaboracion',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]