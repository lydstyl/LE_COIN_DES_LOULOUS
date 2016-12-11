# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nom', models.CharField(default='De naissance à 3 ans', max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('titre', models.CharField(max_length=100)),
                ('photo', models.ImageField(null=True, blank=True, upload_to='photos/')),
                ('presentation', models.TextField(null=True, default='En bon état', blank=True)),
                ('prix', models.DecimalField(null=True, max_digits=5, default=5.0, blank=True, decimal_places=2)),
                ('proprietaire', models.CharField(null=True, default='Amélie', blank=True, max_length=42)),
                ('date', models.DateTimeField(verbose_name='Date de parution', auto_now_add=True)),
                ('age', models.ForeignKey(to='vetements.Age')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nom', models.CharField(default='Vêtement', max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LieuDeStockage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nom', models.CharField(default='Maison Roubaix', max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nom', models.CharField(default='Mixte', max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TypeCategorie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nom', models.CharField(default='Pyjama', max_length=30)),
                ('categorie', models.ForeignKey(to='vetements.Categorie')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='lieu_de_stockage',
            field=models.ForeignKey(to='vetements.LieuDeStockage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='sex',
            field=models.ForeignKey(to='vetements.Sex'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='type_categorie',
            field=models.ForeignKey(to='vetements.TypeCategorie'),
            preserve_default=True,
        ),
    ]
