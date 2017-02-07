# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 15:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_gen', models.CharField(max_length=50)),
                ('nombre_cien', models.CharField(max_length=50)),
                ('taxonomia', models.CharField(max_length=50)),
                ('foto', models.ImageField(null=True, upload_to='avatar')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='especie.Categoria')),
            ],
        ),
    ]
