# Generated by Django 4.0.4 on 2022-06-26 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_alter_publicacion_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='home'),
        ),
    ]
