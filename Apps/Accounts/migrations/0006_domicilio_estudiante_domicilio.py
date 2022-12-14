# Generated by Django 4.1.1 on 2022-10-03 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_alter_estudiante_numcontrol_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=200)),
                ('colonia', models.CharField(max_length=200)),
                ('codigoPostal', models.CharField(max_length=5)),
                ('estado', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='estudiante',
            name='domicilio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Accounts.domicilio'),
        ),
    ]
