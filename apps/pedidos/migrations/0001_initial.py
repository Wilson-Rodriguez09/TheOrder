# Generated by Django 5.1 on 2024-10-17 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField()),
                ('observacion', models.TextField(max_length=600)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
    ]
