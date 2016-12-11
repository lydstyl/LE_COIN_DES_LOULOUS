# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vetements', '0003_exclure'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cocher',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('cocher', models.NullBooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
