# Generated by Django 4.1.3 on 2022-11-14 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('correos', '0003_alter_correspondencia_fecha_recepcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correspondencia',
            name='fecha_recepcion',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
