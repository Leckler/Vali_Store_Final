# Generated by Django 4.0.6 on 2023-06-09 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Documen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=12)),
                ('apellido', models.CharField(max_length=12)),
                ('edad', models.IntegerField(max_length=3)),
                ('email', models.EmailField(max_length=30)),
                ('telefono', models.CharField(max_length=9)),
                ('genero', models.CharField(choices=[(0, 'Seleccione'), (1, 'Masculino'), (2, 'Femenino'), (3, 'Otro')], default=0, max_length=12)),
                ('clave', models.CharField(max_length=12)),
                ('clave1', models.CharField(max_length=12)),
                ('nickname', models.CharField(max_length=12)),
                ('equipo', models.CharField(max_length=12)),
            ],
        ),
    ]
