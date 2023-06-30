# Generated by Django 4.0.6 on 2023-06-29 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Documen', '0022_alter_producto_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='id_producto',
            field=models.AutoField(db_column='idProducto', default=1, primary_key=True, serialize=False, verbose_name='ID_Producto'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]