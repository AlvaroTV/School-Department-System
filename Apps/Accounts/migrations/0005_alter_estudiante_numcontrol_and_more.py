# Generated by Django 4.1.1 on 2022-10-03 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_alter_estudiante_numcontrol_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='numControl',
            field=models.CharField(blank=True, max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='numSeguridadSocial',
            field=models.CharField(blank=True, max_length=70, unique=True),
        ),
    ]
