# Generated by Django 4.1.1 on 2022-11-22 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0089_docente_materias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docente',
            name='materias',
        ),
    ]