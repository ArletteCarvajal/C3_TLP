# Generated by Django 5.0.6 on 2024-07-06 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Operador',
        ),
        migrations.RemoveField(
            model_name='productos',
            name='planta',
        ),
        migrations.RemoveField(
            model_name='registro_produccion',
            name='creado_por',
        ),
        migrations.RemoveField(
            model_name='registro_produccion',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='registro_produccion',
            name='operador',
        ),
        migrations.DeleteModel(
            name='Plantas',
        ),
        migrations.DeleteModel(
            name='Productos',
        ),
        migrations.DeleteModel(
            name='Registro_Produccion',
        ),
    ]