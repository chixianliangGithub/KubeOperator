# Generated by Django 2.1.2 on 2019-09-18 08:29

import common.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kubeops_api', '0014_auto_20190918_0735'),
    ]

    operations = [
        migrations.AddField(
            model_name='deployexecution',
            name='steps',
            field=common.models.JsonListTextField(default=[], null=True),
        ),
    ]