# Generated by Django 4.1.1 on 2022-10-14 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0045_alter_anteproyecto_tipoproyecto'),
    ]

    operations = [
        migrations.CreateModel(
            name='TitularDependencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidoP', models.CharField(max_length=70)),
                ('apellidoM', models.CharField(max_length=70)),
                ('puesto', models.CharField(max_length=50)),
            ],
        ),
    ]