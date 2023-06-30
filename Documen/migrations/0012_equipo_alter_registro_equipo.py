# Generated by Django 4.0.6 on 2023-06-15 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Documen', '0011_remove_registro_id_alter_registro_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('idEquipo', models.AutoField(db_column='idEquipo', primary_key=True, serialize=False, verbose_name='id_equipo')),
                ('equipo', models.CharField(choices=[(0, 'Seleccione'), (1, 'Administrativo'), (2, 'Usuario'), (3, 'Desarrollador')], default=0, max_length=12)),
            ],
        ),
        migrations.AlterField(
            model_name='registro',
            name='equipo',
            field=models.ForeignKey(db_column='idEquipo', on_delete=django.db.models.deletion.CASCADE, to='Documen.equipo'),
        ),
    ]