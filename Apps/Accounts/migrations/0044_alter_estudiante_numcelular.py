# Generated by Django 4.1.1 on 2022-10-13 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0043_alter_estudiante_numcelular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='numCelular',
            field=models.CharField(max_length=20),
        ),
    ]