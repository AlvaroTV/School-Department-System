# Generated by Django 4.1.1 on 2022-10-05 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0016_alter_estudiante_fotousuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='institutoSeguridadSocial',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
