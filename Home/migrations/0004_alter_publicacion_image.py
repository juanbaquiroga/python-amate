# Generated by Django 4.0.4 on 2022-06-26 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_alter_publicacion_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='home/'),
        ),
    ]