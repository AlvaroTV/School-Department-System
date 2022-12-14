# Generated by Django 4.1.1 on 2022-10-06 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0025_remove_expediente_manuadoc_expediente_manualdoc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='expediente',
            name='reporteFinal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Accounts.reportefinal'),
        ),
        migrations.AddField(
            model_name='expediente',
            name='reporteParcial1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Accounts.reporteparcial1'),
        ),
        migrations.AddField(
            model_name='expediente',
            name='reporteParcial2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Accounts.reporteparcial2'),
        ),
    ]
