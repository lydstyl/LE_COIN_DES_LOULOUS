# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vetements', '0007_auto_20141227_1759'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cocher',
        ),
        migrations.RemoveField(
            model_name='filtre',
            name='age',
        ),
        migrations.RemoveField(
            model_name='filtre',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='filtre',
            name='type_categorie',
        ),
        migrations.DeleteModel(
            name='Filtre',
        ),
        migrations.AlterField(
            model_name='exclure',
            name='exclure',
            field=models.CharField(default='a1ea2es2', max_length=30),
            preserve_default=True,
        ),
    ]
