# Generated by Django 5.0.4 on 2024-04-30 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_rename_numero_de_musicos_clase_capacidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='tipo',
            field=models.CharField(choices=[('instrumental', 'Grupo instrumental'), ('con voz', 'Grupo con vocalista')], default='instrumental', max_length=20),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='tipo',
            field=models.CharField(choices=[('instrumental', 'Grupo instrumental'), ('con voz', 'Grupo con vocalista')], max_length=20),
        ),
    ]
