# Generated by Django 4.1.1 on 2022-10-27 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0074_rename_fechaelaboraciona_observaciondocente_fechaelaboracion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='observacion',
            old_name='agregarDias',
            new_name='incrementarDias',
        ),
    ]