# Generated by Django 5.0.6 on 2024-07-06 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0003_rename_nombre_operador_nombre_operador'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plantas',
            old_name='codigo',
            new_name='codigo_planta',
        ),
        migrations.RenameField(
            model_name='plantas',
            old_name='nombre',
            new_name='nombre_planta',
        ),
        migrations.RenameField(
            model_name='productos',
            old_name='codigo',
            new_name='codigo_producto',
        ),
        migrations.RenameField(
            model_name='productos',
            old_name='planta',
            new_name='nombre_planta',
        ),
        migrations.RenameField(
            model_name='productos',
            old_name='nombre',
            new_name='nombre_producto',
        ),
    ]
