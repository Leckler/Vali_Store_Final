# Generated by Django 4.0.6 on 2023-06-17 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Documen', '0017_alter_producto_color_alter_producto_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='nombre',
            field=models.CharField(db_column='idNombre', max_length=12, primary_key=True, serialize=False, verbose_name='ID_Nombre'),
        ),
    ]
