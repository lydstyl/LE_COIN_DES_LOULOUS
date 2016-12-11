# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vetements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filtre',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('age', models.ForeignKey(to='vetements.Age')),
                ('sex', models.ForeignKey(to='vetements.Sex')),
                ('type_categorie', models.ForeignKey(to='vetements.TypeCategorie')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
