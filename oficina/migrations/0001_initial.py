# Generated by Django 5.2 on 2025-04-10 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('carro', models.CharField(max_length=100)),
                ('placa', models.CharField(max_length=10, unique=True)),
            ],
        ),
    ]
