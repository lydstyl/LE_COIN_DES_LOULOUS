# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vetements', '0004_cocher'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocher',
            name='objet',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
    ]
