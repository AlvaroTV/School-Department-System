# Generated by Django 4.1.1 on 2022-10-17 13:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0053_alter_anteproyecto_numintegrantes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anteproyecto',
            name='periodoFin',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='anteproyecto',
            name='periodoInicio',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]