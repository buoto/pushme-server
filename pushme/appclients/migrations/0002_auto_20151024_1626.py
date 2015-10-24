# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import appclients.models


class Migration(migrations.Migration):

    dependencies = [
        ('appclients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='client',
            name='apikey',
            field=models.CharField(default=appclients.models.generate_api_key, max_length=100),
        ),
    ]
