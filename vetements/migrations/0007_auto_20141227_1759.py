# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vetements', '0006_auto_20141227_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocher',
            name='cocher',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
    ]
