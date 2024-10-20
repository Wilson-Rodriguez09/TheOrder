# Generated by Django 5.1.1 on 2024-10-18 19:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
        ('pedidos', '0002_remove_pedidos_cantidad_remove_pedidos_nombre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('observaciones', models.TextField(max_length=600)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cliente.cliente')),
                ('pedidos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pedidos.pedidos')),
            ],
        ),
    ]
