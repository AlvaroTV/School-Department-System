# Generated by Django 4.1.1 on 2022-10-05 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0018_alter_estudiante_domicilio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='fotoUsuario',
            field=models.ImageField(blank=True, default='profilepic.png', null=True, upload_to='profilesPic/'),
        ),
    ]
