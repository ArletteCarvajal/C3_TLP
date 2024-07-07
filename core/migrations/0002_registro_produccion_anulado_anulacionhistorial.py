# Generated by Django 5.0.6 on 2024-07-07 15:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro_produccion',
            name='anulado',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='AnulacionHistorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_anulacion', models.DateTimeField(auto_now_add=True)),
                ('produccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.registro_produccion')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.supervisor')),
            ],
        ),
    ]
