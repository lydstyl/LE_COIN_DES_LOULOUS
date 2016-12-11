# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vetements', '0002_filtre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exclure',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('exclure', models.CharField(max_length=30, default='t1et2et4')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
