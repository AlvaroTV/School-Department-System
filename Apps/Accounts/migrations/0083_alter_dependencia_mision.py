# Generated by Django 4.1.1 on 2022-11-07 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0082_remove_residencia_observaciones_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dependencia',
            name='mision',
            field=models.CharField(max_length=1000),
        ),
    ]
