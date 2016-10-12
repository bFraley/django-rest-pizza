# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topping',
            name='pizza',
            field=models.ForeignKey(to='pizza.Pizza', null=True),
        ),
    ]
