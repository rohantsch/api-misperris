# Generated by Django 2.2.dev20180621213648 on 2018-11-27 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0005_auto_20181029_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascotas',
            name='fotografia',
            field=models.ImageField(upload_to='Imagenes/'),
        ),
    ]