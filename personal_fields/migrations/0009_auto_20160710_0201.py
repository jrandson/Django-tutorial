# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-10 02:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personal_fields', '0008_auto_20160710_0142'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='data_cad',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='form',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='item_field',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='item_field',
            name='select_item',
            field=models.ForeignKey(default=datetime.datetime(2016, 7, 10, 2, 0, 39, 379522, tzinfo=utc), on_delete=django.db.models.deletion.CASCADE, to='personal_fields.Select_item'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item_field',
            name='selected',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='select_item',
            name='form',
            field=models.ForeignKey(default=datetime.datetime(2016, 7, 10, 2, 1, 11, 564208, tzinfo=utc), on_delete=django.db.models.deletion.CASCADE, to='personal_fields.Form'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='select_item',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='text_area',
            name='form',
            field=models.ForeignKey(default=datetime.datetime(2016, 7, 10, 2, 1, 31, 339276, tzinfo=utc), on_delete=django.db.models.deletion.CASCADE, to='personal_fields.Form'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='text_area',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='text_area',
            name='value',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='text_field',
            name='form',
            field=models.ForeignKey(default=datetime.datetime(2016, 7, 10, 2, 1, 47, 147303, tzinfo=utc), on_delete=django.db.models.deletion.CASCADE, to='personal_fields.Form'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='text_field',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='text_field',
            name='value',
            field=models.CharField(default='', max_length=150),
        ),
    ]
