# Generated by Django 4.0.6 on 2023-06-29 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Documen', '0019_suscrito'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='id_producto',
        ),
        migrations.AddField(
            model_name='producto',
            name='id',
            field=models.BigAutoField(auto_created=True, default=2, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
