# Generated by Django 4.1.3 on 2022-11-14 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('correos', '0007_remove_correspondencia_fecha_emtrega'),
    ]

    operations = [
        migrations.AddField(
            model_name='correspondencia',
            name='fecha_entrega',
            field=models.DateField(default=None),
        ),
    ]
