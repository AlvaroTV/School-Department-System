# Generated by Django 4.1.1 on 2022-10-05 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0015_alter_estudiante_fotousuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='fotoUsuario',
            field=models.ImageField(blank=True, default='images/profilepic.png', null=True, upload_to='profilesPic/'),
        ),
    ]
