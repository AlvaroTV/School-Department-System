# Generated by Django 4.1.1 on 2022-10-17 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0058_rename_apellidom_titulardependencia_t_apellidom_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anteproyecto',
            old_name='nombre',
            new_name='a_nombre',
        ),
        migrations.RenameField(
            model_name='dependencia',
            old_name='nombre',
            new_name='d_nombre',
        ),
    ]