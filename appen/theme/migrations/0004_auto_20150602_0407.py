# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0003_auto_20150602_0304'),
    ]

    operations = [
        migrations.CreateModel(
            name='One_comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(),
        ),
        migrations.AddField(
            model_name='one_comment',
            name='the_one',
            field=models.ForeignKey(to='theme.Comment'),
        ),
    ]
