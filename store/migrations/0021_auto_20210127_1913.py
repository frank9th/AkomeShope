# Generated by Django 3.1.5 on 2021-01-27 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_auto_20210127_1855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='price',
            new_name='amount',
        ),
    ]
