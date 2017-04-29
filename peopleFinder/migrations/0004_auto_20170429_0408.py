# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peopleFinder', '0003_auto_20170426_0428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=35)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='state',
            field=models.CharField(default='ZZ', max_length=2),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(default='None', max_length=254),
        ),
        migrations.AddField(
            model_name='field',
            name='person',
            field=models.ManyToManyField(related_name='field_set', to='peopleFinder.Person'),
        ),
    ]
