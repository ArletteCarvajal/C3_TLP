# Generated by Django 5.0.6 on 2024-07-06 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plantas',
            old_name='nomnbre',
            new_name='nombre',
        ),
    ]