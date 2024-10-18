# Generated by Django 5.1.1 on 2024-10-18 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Preparacion',
        ),
    ]
