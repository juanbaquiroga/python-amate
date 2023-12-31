# Generated by Django 4.0.4 on 2022-05-30 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('price', models.FloatField()),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('category', models.CharField(max_length=30)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
