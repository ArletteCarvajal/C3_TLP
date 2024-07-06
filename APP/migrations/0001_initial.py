# Generated by Django 5.0.6 on 2024-07-06 06:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Plantas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomnbre', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('planta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.plantas')),
            ],
        ),
        migrations.CreateModel(
            name='Registro_Produccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('litros_produccion', models.FloatField()),
                ('fecha_produccion', models.DateField()),
                ('turno', models.CharField(choices=[('mañana', 'AM'), ('tarde', 'PM'), ('noche', 'MM')], max_length=6)),
                ('hora_registro', models.TimeField()),
                ('codigo_combustible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.productos')),
                ('operador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.operador')),
            ],
        ),
    ]
