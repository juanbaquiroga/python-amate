# Generated by Django 4.0.4 on 2022-06-05 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0004_categoria_remove_producto_category_producto_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='category',
        ),
        migrations.AddField(
            model_name='producto',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Productos.categoria'),
            preserve_default=False,
        ),
    ]
