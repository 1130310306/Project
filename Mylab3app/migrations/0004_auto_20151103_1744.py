# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mylab3app', '0003_auto_20151102_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='PublishDate',
            field=models.DateField(),
        ),
    ]
