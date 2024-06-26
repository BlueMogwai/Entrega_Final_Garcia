# Generated by Django 5.0.4 on 2024-04-30 10:59

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('size', models.CharField(choices=[('duo', 'duo'), ('trio', 'trio'), ('cuarteto', 'cuarteto'), ('combo', 'combo')], default='combo', max_length=20)),
                ('tipo', models.CharField(choices=[('instrumental', 'Grupo instrumental'), ('convoz', 'Grupo con vocalista')], default='instrumental', max_length=20)),
                ('descripcion', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('duo', 'duo'), ('trio', 'trio'), ('cuarteto', 'cuarteto'), ('combo', 'combo')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('instrumental', 'Grupo instrumental'), ('convoz', 'Grupo con vocalista')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('disponible', models.BooleanField(default=True)),
                ('numero_de_musicos', models.IntegerField()),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grupo', to='bookings.grupo')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('instrumento', models.CharField(max_length=50)),
                ('seccion', models.CharField(max_length=50)),
                ('experiencia', models.BooleanField(default=True)),
                ('presentacion', models.TextField(max_length=500)),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('hora_inicio', models.TimeField(default=django.utils.timezone.now)),
                ('hora_fin', models.TimeField(default=django.utils.timezone.now)),
                ('clase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservas', to='bookings.clase')),
            ],
        ),
    ]
