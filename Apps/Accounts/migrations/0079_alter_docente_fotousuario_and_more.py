# Generated by Django 4.1.1 on 2022-10-27 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0078_alter_expediente_estatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='fotoUsuario',
            field=models.ImageField(blank=True, default='profilepicD.jpg', null=True, upload_to='profilesPic/teachers/'),
        ),
        migrations.AlterField(
            model_name='observaciondocente',
            name='observacionD',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]