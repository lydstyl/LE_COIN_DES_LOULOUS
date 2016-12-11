# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vetements', '0005_cocher_objet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cocher',
            name='objet',
        ),
        migrations.AlterField(
            model_name='cocher',
            name='cocher',
            field=models.NullBooleanField(verbose_name='Féminin'),
            preserve_default=True,
        ),
    ]
