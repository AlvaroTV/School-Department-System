# Generated by Django 4.1.1 on 2022-10-04 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0008_reportefinal_reporteparcial1_reporteparcial2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='expediente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Accounts.expediente'),
        ),
    ]
