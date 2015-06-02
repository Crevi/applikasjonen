# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0004_auto_20150602_0407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='one_comment',
            name='the_one',
        ),
        migrations.DeleteModel(
            name='One_comment',
        ),
    ]
