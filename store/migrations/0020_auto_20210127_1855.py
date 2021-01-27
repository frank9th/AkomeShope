# Generated by Django 3.1.5 on 2021-01-27 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_auto_20210127_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.customer'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='is_ordered',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
