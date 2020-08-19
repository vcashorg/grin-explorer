# Generated by Django 2.1.1 on 2020-08-19 03:19

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0018_block_kernel_mmr_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='block',
            name='edge_bits',
        ),
        migrations.RemoveField(
            model_name='block',
            name='secondary_scaling',
        ),
        migrations.RemoveField(
            model_name='block',
            name='total_difficulty',
        ),
        migrations.AddField(
            model_name='block',
            name='btc_header_hash',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='block',
            name='pow_hash',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='cuckoo_solution',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='block',
            name='nonce',
            field=models.TextField(null=True),
        ),
    ]