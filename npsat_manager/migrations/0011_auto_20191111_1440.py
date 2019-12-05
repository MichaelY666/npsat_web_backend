# Generated by Django 2.2.5 on 2019-11-11 22:40

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('npsat_manager', '0010_auto_20191111_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelrun',
            name='county',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='model_runs', to='npsat_manager.County'),
        ),
        migrations.AlterField(
            model_name='modelrun',
            name='date_run',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 11, 22, 40, 48, 533562, tzinfo=utc), null=True),
        ),
    ]