# Generated by Django 2.0 on 2018-09-03 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0007_block_cuckoo_solution'),
    ]

    operations = [
        migrations.AddField(
            model_name='output',
            name='block_height',
            field=models.IntegerField(null=True),
        ),
    ]
