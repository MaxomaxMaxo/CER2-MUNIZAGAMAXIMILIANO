# Generated by Django 4.1.3 on 2022-11-14 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('correos', '0002_correspondencia_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correspondencia',
            name='fecha_recepcion',
            field=models.DateField(auto_now_add=True),
        ),
    ]
