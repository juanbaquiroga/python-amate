# Generated by Django 4.0.4 on 2022-06-27 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0009_remove_producto_imagen_producto_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='image',
            new_name='imagen',
        ),
    ]
