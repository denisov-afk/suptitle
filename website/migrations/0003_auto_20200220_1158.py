# Generated by Django 3.0.3 on 2020-02-20 08:58

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20200219_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='aspect_ratio',
            field=models.CharField(default='on process', max_length=100),
        ),
        migrations.AlterField(
            model_name='video',
            name='background_color',
            field=models.CharField(default='on process', max_length=100),
        ),
        migrations.AlterField(
            model_name='video',
            name='caption_position_h',
            field=models.CharField(choices=[('L', 'Left'), ('R', 'Right'), ('C', 'Center')], default='C', max_length=1),
        ),
        migrations.AlterField(
            model_name='video',
            name='caption_position_v',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='video',
            name='caption_style',
            field=models.CharField(default='on process', max_length=100),
        ),
        migrations.AlterField(
            model_name='video',
            name='captions',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='headline',
            field=models.CharField(default='Headline', max_length=100),
        ),
        migrations.AlterField(
            model_name='video',
            name='headline_position_h',
            field=models.CharField(choices=[('L', 'Left'), ('R', 'Right'), ('C', 'Center')], default='C', max_length=1),
        ),
        migrations.AlterField(
            model_name='video',
            name='headline_position_v',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='video',
            name='headline_style',
            field=models.CharField(default='on process', max_length=100),
        ),
        migrations.AlterField(
            model_name='video',
            name='uploaded',
            field=models.DateTimeField(auto_created=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='zoom',
            field=models.IntegerField(default=1),
        ),
    ]
