# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appclients', '0002_auto_20151024_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
