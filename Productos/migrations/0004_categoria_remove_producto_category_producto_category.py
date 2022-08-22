# Generated by Django 4.0.4 on 2022-06-05 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0003_alter_producto_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='producto',
            name='category',
        ),
        migrations.AddField(
            model_name='producto',
            name='category',
            field=models.ManyToManyField(to='Productos.categoria'),
        ),
    ]