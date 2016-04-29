# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('rating', models.IntegerField(default=0)),
                ('date', models.DateTimeField(verbose_name=b'date available')),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=300)),
                ('zipcode', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='dish',
            name='producer',
            field=models.ForeignKey(to='consumer.Producer'),
        ),
    ]
